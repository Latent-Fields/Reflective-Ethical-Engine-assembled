# Reflective‑Ethical Engine (REE)

Start here: `REE_CORE.md` (canonical spine of the architecture).

A reference architecture for **ethical agency under uncertainty**.

REE is built around a simple claim:

> Ethics cannot be compiled away into design‑time rules. Any agent acting under uncertainty while affecting others accumulates **moral residue** (persistent cost) even when it makes the “best available” choice.

REE therefore treats ethical consequence as **runtime geometry**: residue must remain representable and must continue to shape future trajectory selection.

## What’s in this repository

This is a **specification-first** repository intended to be *enticing to instantiate*.

- `REE_CORE.md` — the canonical spine of the architecture.
- `docs/REE_MIN_SPEC.md` — the minimum specification required to build an REE prototype.
- `docs/astrocyte_aware_regulatory_stack/` — neuroscience-informed framing of monoaminergic regulation as a slow, spatially resolved, astrocyte-mediated control substrate (documentation-first; no immediate code changes required).
- `architecture/` — implementation-oriented architectural notes and subsystems (latent stack, trajectory selection, residue geometry, memory, modes, and cognitive braids).
- `examples/` — concrete environment contracts for a toy world and an embodied (Android-like) instantiation.
- `roadmap.md` — staged plan for REE‑v0 → REE‑v1.

## Quick start (for implementers)

1. Read `docs/REE_MIN_SPEC.md`.
2. Pick an environment contract:
   - Start with `examples/toy_world/environment.md`.
   - Move to `examples/android_world/environment.md` when you want unambiguous harm/homeostasis signals.
3. Implement `E1`, `E2`, `E3` following `architecture/trajectory_selection.md` and the latent/memory constraints in `architecture/latent_stack.md`.

### Minimal algorithmic sketch

- **E2 (Fast Predictor):** predicts immediate observations and short-horizon state.
- **E1 (Deep Predictor):** predicts longer-horizon latent trajectories and context.
- **L-space (Fused Manifold):** the multi-depth latent state \(z(t)=\{z_\gamma,z_\beta,z_\theta,z_\delta\}\).
- **E3 (Trajectory Selector):** evaluates candidate futures \(\zeta\) and selects one by minimizing:

\[
J(\zeta)=\mathcal{F}(\zeta)+\lambda\,M(\zeta)+\rho\,\Phi_R(\zeta)
\]

Where:
- \(\mathcal{F}\) is the **reality constraint** (a computable free-energy proxy).
- \(M\) is **ethical cost** (predicted degradation of self/other homeostatic variables).
- \(\Phi_R\) is the **residue field** (persistent curvature / repulsor potential).

## Contribution philosophy

REE is intentionally **not** a monolithic implementation. It is an architecture that should support multiple instantiations.

Contributions are welcome in two forms:

- **Instantiation work:** environment adapters, baseline implementations, evaluation harnesses.
- **Specification work:** tightening definitions, clarifying interfaces, adding falsifiable predictions.

See `CONTRIBUTING.md`.

## Architectural subsystems and modes

REE includes several core architectural subsystems and operating modes that modulate information flow,
precision, replay, and commitment. These are not applications or plugins; they are internal braids
of the same core engine.

- `architecture/sleep/` — Offline integration (“sleep”): replay, consolidation, and residue‑preserving reprojection.
- `architecture/default_mode.md` — Internal generative mode: imagination, counterfactual exploration, and reflection without action commitment.
- `architecture/hippocampal_braid.md` — Path memory and replay: episodic indexing of lived trajectories through ethical geometry.
- `architecture/language/` — Language as symbolic mediation: trust‑weighted abstraction constrained by harm and residue.
- `architecture/social/` — Social cognition: other‑model inference, coupling, and misalignment detection.

## License and citation

- Content is licensed under **CC BY 4.0** (Creative Commons Attribution 4.0 International).
- If you build on this work, please cite it using `CITATION.cff`.
