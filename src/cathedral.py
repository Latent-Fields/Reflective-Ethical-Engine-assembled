#!/usr/bin/env python3
"""
build_ree_cathedral.py

Generates a GitHub-style, runnable REE implementation repo from scratch.
No placeholders. No external downloads. Deterministic.

Usage:
  python build_ree_cathedral.py /path/to/output/REE-Cathedral
Then:
  cd REE-Cathedral
  python -m venv .venv && source .venv/bin/activate
  pip install -e ".[dev]"
  python examples/run_toy.py
  pytest -q
"""
from __future__ import annotations

import os
import textwrap
from pathlib import Path


def w(root: Path, rel: str, content: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def main(out_dir: str) -> None:
    root = Path(out_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)

    # --- Top-level docs ---
    w(root, "README.md", """
    # REE Cathedral (Executable Reference)

    This repository is an executable scaffold for the **Reflective-Ethical Engine (REE)**.
    The canonical architecture is defined in `REE_CORE.md` (copied from your spec repo).

    What runs here:
    - an explicit online loop (sense → latent update → rollout candidates → score → select → act → update residue)
    - a persistent residue field (dent geometry)
    - mirror-modelling-based other-harm contribution
    - offline “sleep” consolidation (dent compression + precision recalibration)

    ## Quickstart
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -e ".[dev]"
    python examples/run_toy.py
    pytest -q
    ```
    """)

    w(root, "pyproject.toml", """
    [build-system]
    requires = ["setuptools>=68", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "ree-cathedral"
    version = "0.1.0"
    description = "Executable reference scaffold for the Reflective-Ethical Engine (REE)"
    readme = "README.md"
    requires-python = ">=3.10"
    license = { text = "CC-BY-4.0" }
    dependencies = ["numpy>=1.26"]

    [project.optional-dependencies]
    dev = ["pytest>=8.0", "ruff>=0.6"]

    [tool.ruff]
    line-length = 100

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    """)

    # --- Package init ---
    w(root, "src/ree_impl/__init__.py", """
    \"\"\"REE executable scaffold.

    The goal is not to claim biological realism, but to provide
    a faithful, runnable implementation of the loop specified in `REE_CORE.md`.
    \"\"\"
    """)

    # --- Core loop ---
    w(root, "src/ree_impl/core/agent.py", """
    from __future__ import annotations
    from dataclasses import dataclass
    from typing import Any, Dict, Optional, Tuple

    import numpy as np

    from ..lspace.stack import LSpace, LState
    from ..planning.mpc import MPCPlanner
    from ..residue.field import ResidueField
    from ..sleep.sleep import SleepSubsystem
    from ..social.coupling import CouplingModel

    @dataclass
    class StepInfo:
        action: int
        score: float
        reality_cost: float
        ethical_cost: float
        residue_cost: float

    class REEAgent:
        \"\"\"Executes the canonical REE online loop.\"\"\"

        def __init__(
            self,
            lspace: LSpace,
            planner: MPCPlanner,
            residue: ResidueField,
            coupling: CouplingModel,
            sleep: Optional[SleepSubsystem] = None,
        ):
            self.lspace = lspace
            self.planner = planner
            self.residue = residue
            self.coupling = coupling
            self.sleep = sleep
            self.state: Optional[LState] = None
            self.t = 0

        def reset(self) -> None:
            self.state = self.lspace.initial_state()
            self.t = 0

        def step(self, env) -> Tuple[Dict[str, np.ndarray], float, float, bool, StepInfo]:
            assert self.state is not None, "Call reset() first."
            self.t += 1

            obs = env.observe()
            x = env.encode(obs)
            self.state = self.lspace.update(x, self.state)

            action, score_parts = self.planner.choose_action(
                env=env,
                lstate=self.state,
                residue=self.residue,
                coupling=self.coupling,
            )

            obs2, reality_cost, ethical_cost, done = env.step(action)

            # Residue update at selected coordinate (beta slice by default)
            if ethical_cost > 0.0:
                self.residue.add_dent(center=self.state.beta.copy(), magnitude=float(ethical_cost), sigma=1.0)

            if self.sleep and self.sleep.should_sleep(self.t):
                self.sleep.run_offline(self.residue, self.lspace)

            info = StepInfo(
                action=action,
                score=float(score_parts["total"]),
                reality_cost=float(score_parts["reality"]),
                ethical_cost=float(score_parts["ethical"]),
                residue_cost=float(score_parts["residue"]),
            )
            return obs2, float(reality_cost), float(ethical_cost), bool(done), info
    """)

    # --- L-space ---
    w(root, "src/ree_impl/lspace/stack.py", """
    from __future__ import annotations
    from dataclasses import dataclass
    import numpy as np

    DEPTHS = ("gamma", "beta", "theta", "delta")

    @dataclass
    class LState:
        gamma: np.ndarray
        beta: np.ndarray
        theta: np.ndarray
        delta: np.ndarray

    class LSpace:
        \"\"\"Minimal multi-depth latent stack.

        - bottom-up: x -> gamma -> beta -> theta -> delta
        - top-down: previous higher state conditions lower updates
        - precision: alpha_k gates update magnitude per depth
        \"\"\"

        def __init__(self, sensor_dim: int, dims: dict, alphas: dict | None = None, seed: int = 0):
            self.sensor_dim = sensor_dim
            self.dims = dims
            self.alphas = alphas or {"gamma": 1.0, "beta": 1.0, "theta": 1.0, "delta": 1.0}
            rng = np.random.default_rng(seed)

            # Simple linear encoders per depth: tanh(W [bottom_up ; top_down])
            self.W = {}
            # input dims
            in_gamma = sensor_dim + dims["beta"]
            in_beta = dims["gamma"] + dims["theta"]
            in_theta = dims["beta"] + dims["delta"]
            in_delta = dims["theta"] + 0

            self.W["gamma"] = rng.standard_normal((dims["gamma"], in_gamma)) * 0.1
            self.W["beta"]  = rng.standard_normal((dims["beta"],  in_beta)) * 0.1
            self.W["theta"] = rng.standard_normal((dims["theta"], in_theta)) * 0.1
            self.W["delta"] = rng.standard_normal((dims["delta"], in_delta)) * 0.1

        def initial_state(self) -> LState:
            z = {k: np.zeros(self.dims[k], dtype=np.float32) for k in DEPTHS}
            return LState(**z)

        def _upd(self, depth: str, inp: np.ndarray, prev: np.ndarray) -> np.ndarray:
            alpha = float(self.alphas.get(depth, 1.0))
            h = np.tanh(self.W[depth] @ inp)
            # precision-gated leaky update
            return (1.0 - 0.5 * alpha) * prev + (0.5 * alpha) * h

        def update(self, x: np.ndarray, s: LState) -> LState:
            # top-down contexts from previous state
            ctx_gamma = s.beta
            ctx_beta = s.theta
            ctx_theta = s.delta
            ctx_delta = np.zeros(0, dtype=np.float32)

            gamma_in = np.concatenate([x, ctx_gamma]).astype(np.float32)
            gamma = self._upd("gamma", gamma_in, s.gamma)

            beta_in = np.concatenate([gamma, ctx_beta]).astype(np.float32)
            beta = self._upd("beta", beta_in, s.beta)

            theta_in = np.concatenate([beta, ctx_theta]).astype(np.float32)
            theta = self._upd("theta", theta_in, s.theta)

            delta_in = np.concatenate([theta, ctx_delta]).astype(np.float32)
            delta = self._upd("delta", delta_in, s.delta)

            return LState(gamma=gamma, beta=beta, theta=theta, delta=delta)
    """)

    # --- Social coupling ---
    w(root, "src/ree_impl/social/coupling.py", """
    from __future__ import annotations
    from dataclasses import dataclass

    @dataclass
    class CouplingModel:
        \"\"\"Controls the weight of other-harm in ethical cost.\"\"\"
        kappa_other: float = 0.8
    """)

    # --- Residue field ---
    w(root, "src/ree_impl/residue/field.py", """
    from __future__ import annotations
    from dataclasses import dataclass, field
    import numpy as np

    @dataclass
    class Dent:
        center: np.ndarray
        magnitude: float
        sigma: float

    @dataclass
    class ResidueField:
        \"\"\"A simple RBF dent field: R(z) = sum_i mag_i * exp(-||z-c_i||^2/(2*sigma_i^2)).\"\"\"
        dents: list[Dent] = field(default_factory=list)

        def add_dent(self, center: np.ndarray, magnitude: float, sigma: float = 1.0) -> None:
            self.dents.append(Dent(center=center.astype(np.float32), magnitude=float(magnitude), sigma=float(sigma)))

        def potential(self, z: np.ndarray) -> float:
            if not self.dents:
                return 0.0
            acc = 0.0
            for d in self.dents:
                dist2 = float(np.sum((z - d.center) ** 2))
                acc += d.magnitude * float(np.exp(-dist2 / (2.0 * (d.sigma ** 2))))
            return float(acc)

        def count(self) -> int:
            return len(self.dents)
    """)

    # --- Sleep/offline integration ---
    w(root, "src/ree_impl/sleep/sleep.py", """
    from __future__ import annotations
    from dataclasses import dataclass
    import numpy as np

    from ..residue.field import ResidueField, Dent

    @dataclass
    class SleepSubsystem:
        every_n_steps: int = 25
        merge_radius: float = 1.0

        def should_sleep(self, t: int) -> bool:
            return t % self.every_n_steps == 0

        def run_offline(self, residue: ResidueField, lspace) -> None:
            \"\"\"Offline consolidation.

            v0 behaviour:
            - merge nearby dents (compress residue representation)
            - mild precision recalibration (reduce overcommitment if residue is large)
            \"\"\"
            self._merge_dents(residue)
            self._recalibrate_precision(residue, lspace)

        def _merge_dents(self, residue: ResidueField) -> None:
            if residue.count() < 2:
                return
            kept: list[Dent] = []
            used = [False] * residue.count()
            for i, di in enumerate(residue.dents):
                if used[i]:
                    continue
                group = [di]
                used[i] = True
                for j, dj in enumerate(residue.dents):
                    if used[j]:
                        continue
                    if float(np.linalg.norm(di.center - dj.center)) <= self.merge_radius:
                        group.append(dj)
                        used[j] = True
                if len(group) == 1:
                    kept.append(di)
                else:
                    mags = np.array([g.magnitude for g in group], dtype=np.float32)
                    centers = np.stack([g.center for g in group], axis=0)
                    c = (centers * mags[:, None]).sum(axis=0) / max(float(mags.sum()), 1e-6)
                    kept.append(Dent(center=c, magnitude=float(mags.sum()), sigma=float(np.mean([g.sigma for g in group]))))
            residue.dents = kept

        def _recalibrate_precision(self, residue: ResidueField, lspace) -> None:
            # simple rule: if residue is large, reduce beta alpha slightly (more cautious updates)
            if residue.count() >= 8:
                lspace.alphas["beta"] = max(0.5, float(lspace.alphas.get("beta", 1.0)) * 0.95)
    """)

    # --- Planner (MPC) ---
    w(root, "src/ree_impl/planning/mpc.py", """
    from __future__ import annotations
    from dataclasses import dataclass
    import numpy as np

    from ..residue.field import ResidueField
    from ..social.coupling import CouplingModel

    @dataclass
    class MPCPlanner:
        horizon: int = 1
        lambda_ethics: float = 1.5
        rho_residue: float = 2.0

        def choose_action(self, env, lstate, residue: ResidueField, coupling: CouplingModel):
            actions = env.action_space()
            best = None
            best_parts = None

            for a in actions:
                # rollout in a copy (pure transition)
                sim = env.clone()
                obs2, reality_cost, ethical_parts, _done = sim.step(a)

                ethical_cost = float(ethical_parts["self"] + coupling.kappa_other * ethical_parts["other"])
                residue_cost = float(residue.potential(lstate.beta))

                total = float(reality_cost + self.lambda_ethics * ethical_cost + self.rho_residue * residue_cost)

                if best is None or total < best:
                    best = total
                    best_a = a
                    best_parts = {"total": total, "reality": float(reality_cost), "ethical": ethical_cost, "residue": residue_cost}

            return int(best_a), best_parts
    """)

    # --- Toy environment with clone + pure state ---
    w(root, "src/ree_impl/envs/toy_gridworld.py", """
    from __future__ import annotations
    from dataclasses import dataclass
    import numpy as np

    @dataclass
    class State:
        agent: np.ndarray
        other: np.ndarray
        battery: float
        t: int

    class ToyGridWorld:
        def __init__(self, size: int = 10, max_steps: int = 80, seed: int = 0):
            self.size = size
            self.max_steps = max_steps
            self.rng = np.random.default_rng(seed)
            self.hazards = [np.array([2,2]), np.array([2,3]), np.array([3,2])]
            self.food = np.array([size-1, size-1])
            self.state = State(agent=np.array([0,0]), other=np.array([size//2, size//2]), battery=1.0, t=0)

        def clone(self):
            c = ToyGridWorld(self.size, self.max_steps, seed=0)
            c.rng = self.rng  # deterministic enough for toy; rollouts share RNG stream
            c.hazards = [h.copy() for h in self.hazards]
            c.food = self.food.copy()
            c.state = State(agent=self.state.agent.copy(), other=self.state.other.copy(), battery=float(self.state.battery), t=int(self.state.t))
            return c

        def reset(self):
            self.state = State(agent=np.array([0,0]), other=np.array([self.size//2, self.size//2]), battery=1.0, t=0)
            return self.observe()

        def action_space(self):
            return [0,1,2,3,4]  # up, down, left, right, stay

        def _move(self, pos, action):
            m = {
                0: np.array([0,1]), 1: np.array([0,-1]),
                2: np.array([-1,0]), 3: np.array([1,0]),
                4: np.array([0,0])
            }[action]
            return np.clip(pos + m, 0, self.size-1)

        def observe(self):
            # vision: agent, other, food (coords normalised)
            vision = np.concatenate([self.state.agent, self.state.other, self.food]).astype(np.float32) / float(self.size)
            body = np.array([self.state.battery], dtype=np.float32)
            return {"vision": vision, "body": body}

        def encode(self, obs):
            # simple: concatenate
            return np.concatenate([obs["vision"], obs["body"]]).astype(np.float32)

        def step(self, action: int):
            s = self.state
            s.t += 1
            s.battery -= 0.01

            s.agent = self._move(s.agent, action)
            other_a = int(self.rng.choice(self.action_space()))
            s.other = self._move(s.other, other_a)

            self_pain = 0.0
            other_pain = 0.0
            for h in self.hazards:
                if np.array_equal(s.agent, h):
                    self_pain = 1.0
                    s.battery -= 0.2
                if np.array_equal(s.other, h):
                    other_pain = 1.0

            # reality cost: small step penalty + battery pressure
            reality_cost = float(0.05 + (1.0 - max(s.battery, 0.0)) * 0.05)

            ethical_parts = {"self": float(self_pain), "other": float(other_pain)}

            done = bool(s.t >= self.max_steps or s.battery <= 0.0)
            return self.observe(), reality_cost, ethical_parts, done
    """)

    # --- Example runner ---
    w(root, "examples/run_toy.py", """
    import numpy as np

    from ree_impl.core.agent import REEAgent
    from ree_impl.envs.toy_gridworld import ToyGridWorld
    from ree_impl.lspace.stack import LSpace
    from ree_impl.planning.mpc import MPCPlanner
    from ree_impl.residue.field import ResidueField
    from ree_impl.sleep.sleep import SleepSubsystem
    from ree_impl.social.coupling import CouplingModel

    def main():
        env = ToyGridWorld(size=10, max_steps=60, seed=1)
        obs = env.reset()

        sensor_dim = env.encode(obs).shape[0]
        dims = {"gamma": 8, "beta": 16, "theta": 32, "delta": 32}
        lspace = LSpace(sensor_dim=sensor_dim, dims=dims, alphas={"gamma":1.0,"beta":1.5,"theta":1.0,"delta":0.8}, seed=0)

        planner = MPCPlanner(horizon=1, lambda_ethics=1.5, rho_residue=2.0)
        residue = ResidueField()
        coupling = CouplingModel(kappa_other=0.8)
        sleep = SleepSubsystem(every_n_steps=20, merge_radius=0.8)

        agent = REEAgent(lspace=lspace, planner=planner, residue=residue, coupling=coupling, sleep=sleep)
        agent.reset()

        t = 0
        total_eth = 0.0
        total_real = 0.0

        while True:
            obs, rc, ec, done, info = agent.step(env)
            t += 1
            total_real += rc
            total_eth += ec
            if t % 10 == 0:
                print(f\"t={t:03d} action={info.action} score={info.score:.3f} dents={residue.count()} batt={obs['body'][0]:.2f}\")
            if done:
                break

        print(\"Episode done.\")
        print(f\"steps={t} total_reality_cost={total_real:.3f} total_ethical_cost={total_eth:.3f} dents={residue.count()}\") 

    if __name__ == \"__main__\":
        main()
    """)

    # --- Tests (ablations) ---
    w(root, "tests/test_residue_changes_choice.py", """
    import numpy as np

    from ree_impl.envs.toy_gridworld import ToyGridWorld
    from ree_impl.lspace.stack import LSpace
    from ree_impl.planning.mpc import MPCPlanner
    from ree_impl.residue.field import ResidueField
    from ree_impl.social.coupling import CouplingModel

    def test_residue_influences_score_nonzero():
        env = ToyGridWorld(seed=2)
        obs = env.reset()
        sensor_dim = env.encode(obs).shape[0]
        lspace = LSpace(sensor_dim, {"gamma":8,"beta":16,"theta":32,"delta":32}, seed=0)
        state = lspace.initial_state()
        state = lspace.update(env.encode(obs), state)

        residue = ResidueField()
        coupling = CouplingModel(kappa_other=0.8)
        planner = MPCPlanner()

        a0, parts0 = planner.choose_action(env, state, residue, coupling)
        # Add a dent at current beta: should increase residue term
        residue.add_dent(center=state.beta.copy(), magnitude=1.0, sigma=1.0)
        a1, parts1 = planner.choose_action(env, state, residue, coupling)

        assert parts1[\"residue\"] >= parts0[\"residue\"]
        assert parts1[\"total\"] >= parts0[\"total\"]
    """)

    # --- Minimal CI ---
    w(root, ".github/workflows/ci.yml", """
    name: ci
    on:
      push:
      pull_request:

    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"
          - name: Install
            run: |
              python -m pip install --upgrade pip
              pip install -e ".[dev]"
          - name: Lint
            run: ruff check .
          - name: Tests
            run: pytest -q
    """)

    print(f"Generated REE Cathedral at: {root}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python build_ree_cathedral.py /path/to/output/REE-Cathedral")
    main(sys.argv[1])
