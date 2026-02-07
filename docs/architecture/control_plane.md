# Control Plane — Precision, Gain, and Mode Regulation

**Claim Type:** architectural_commitment  
**Scope:** control_plane  
**Depends On:** [INV-005](../invariants.md#inv-005), [INV-006](../invariants.md#inv-006), [INV-009](../invariants.md#inv-009)  
**Status:** stable

---

> The control plane in the Reflective Ethical Engine (REE) governs **how the system operates**, not *what it represents*. It modulates precision, gain, exploration, replay, and commitment thresholds across the architecture.

**Source:** This is a canonical lift from [../../architecture/control_plane.md](../../architecture/control_plane.md)

---

## Summary

The control plane does **not**:
- overwrite representational content,
- select actions directly, or
- compute reward or value.

Its function is to tune information flow so that prediction, imagination, commitment, and learning occur in the appropriate regime.

---

## Architectural Necessity

Given REE constraints:
- perception completes at the shared sensory latent z_S,
- belief update occurs only after commitment (E3),
- imagination must be possible without belief update,
- ethical residue φ(z) must remain path dependent and non-optimisable,

there must exist a mechanism that:
1. regulates the **precision** of prediction errors at different depths,
2. controls **when commitment is possible or suppressed**,
3. adjusts **exploration horizon and branching** in fast rollouts,
4. schedules **replay and consolidation**, and
5. switches between operating modes (task-engaged, Default Mode–like, sleep/offline).

**This mechanism is the control plane.**

**Related Claims:** [INV-005](../invariants.md#inv-005), [INV-009](../invariants.md#inv-009)

---

## Control Surface

The control plane operates over a structured set of tunable parameters exposed by REE modules:

**Control-plane modulation is differential rather than global:** precision, gain, horizon, replay, and commitment parameters may be increased in some subsystems while simultaneously decreased or stabilised in others.

There is no single global arousal or confidence variable; tuning is depth- and module-specific.

### Tunable Parameters (Illustrative)

θ_tune = {
  α_S,      // sensory prediction-error precision
  g_S,      // sensory gain (attention-like modulation)
  α_A,      // action/policy precision
  κ_commit, // commitment threshold (E3)
  τ_E2,     // rollout temperature
  H,        // rollout horizon
  N,        // number of candidate futures
  η_E1,     // E1 learning-rate rigidity/plasticity
  η_E2,     // E2 learning-rate rigidity/plasticity
  g_replay, // replay rate (hippocampal braid)
  b_completion, // pattern-completion bias
  m         // operating mode flag
}

The control plane updates θ_tune continuously based on context, urgency, residue curvature, and predicted risk or harm.

**See:** [../../architecture/precision_control.md](../../architecture/precision_control.md) for detailed precision mechanics

---

## Relationship to E3

E3 instantiates the **decision logic** of the control plane.

- The **commitment gate** selects and stabilises a future trajectory.
- The **control plane** determines whether commitment is permitted, deferred, or suppressed, and how strongly prediction errors should influence learning.

**E3 therefore acts as the *epistemic liability gate* of the system:** it decides when outcomes become attributable and belief-updating.

**See:** [e3.md](e3.md)

---

## Operating Modes

The control plane supports distinct operating regimes through coordinated tuning of parameters.

### Task-Engaged Mode
- High sensory precision and gain
- Normal or lowered commitment threshold
- Limited replay
- Learning enabled

**Used when:** accurate perception and timely action are required.

---

### Default Mode–like (Internal Generative) Mode
- Reduced sensory precision
- Elevated replay and pattern completion
- Suppressed commitment (high κ_commit)
- Learning and belief update suspended

**Supports:** imagination, counterfactual exploration, autobiographical reflection, and planning without action.

**See:** [../../architecture/Default_mode.md](../../architecture/Default_mode.md)

**Related Claims:** [INV-008](../invariants.md#inv-008)

---

### Sleep / Offline Mode
- Minimal sensory influence
- High replay scheduling
- Consolidation and structural reorganisation
- No commitment or belief update

**Supports:** long-term integration while preserving ethical residue and perceptual corrigibility.

**See:** [../../architecture/sleep/](../../architecture/sleep/)

**Related Claims:** [INV-007](../invariants.md#inv-007)

---

## Neuromodulatory Analogy (Functional, Not Literal)

Biological neuromodulatory systems can be understood as implementing aspects of such a control plane.

In REE, these are treated as **functional control channels**, not biological claims:

- **Dopamine-like:** commitment strength and policy precision
- **Acetylcholine-like:** sensory gain and attentional weighting
- **Serotonin-like:** model stability, patience, and resistance to impulsive updating
- **Noradrenergic-like:** urgency, interrupt, and rapid engagement
- **Histamine-like:** global availability and throughput (arousal)

These channels alter *how cognition runs*, not *what it represents*.

**See:** [../astrocyte_aware_regulatory_stack/](../astrocyte_aware_regulatory_stack/) for neuroscience-informed elaboration

---

## Safety Constraints

The control plane must satisfy:

### 1. No Representational Overwrite
Tuning alters influence and scheduling, not latent content.

**Related:** Perceptual corrigibility

---

### 2. Commitment Gating
Belief update and ethical attribution occur only after E3 commitment.

**Related Claims:** [INV-009](../invariants.md#inv-009)

---

### 3. Residue Preservation
Replay and mode switching must not erase or flatten ethical curvature.

**Related Claims:** [INV-003](../invariants.md#inv-003)

---

### 4. Hypothesis Tagging
Outputs generated outside commitment are explicitly non-committal.

**Related Claims:** [INV-008](../invariants.md#inv-008)

---

These constraints prevent imagination from becoming delusion and urgency from becoming compulsion.

---

## Interpretation

The control plane explains why emotion, arousal, and attention feel like changes in *how thinking works* rather than changes in belief.

It provides the mechanism by which the Self:
- remains coherent in the present,
- explores possible futures safely,
- commits under uncertainty, and
- learns responsibly from consequences.

---

## Summary Statement

The control plane is the regulatory substrate of REE.

It:
- governs operating regimes without overwriting content,
- enables mode switching between action, imagination, and consolidation,
- implements depth-specific precision control,
- and maintains safety constraints across all operating modes.

**The control plane is not "on top of" the system — it is woven throughout it.**

---

## Open Questions

- What is the minimal set of control channels for REE compliance? *(OPEN-006)*
- How should control plane parameters be initialised for new agents? *(IMPL-040)*
- Can control plane dynamics be learned end-to-end? *(MECH-045)*

---

## Related Claims

- **INV-005:** Depth-specific precision routing — control plane implements this
- **INV-006:** Attention as precision modulation — control plane mechanism
- **INV-007:** Offline integration requirement — sleep mode implementation
- **INV-008:** Imagination without belief update — Default Mode implementation
- **INV-009:** Commitment-gated responsibility — commitment threshold control
- **ARCH-008:** Mode-dependent control parameter sets

---

## References / Source Fragments

**Primary Source:** [../../architecture/control_plane.md](../../architecture/control_plane.md) — Content lifted verbatim with claim metadata added

**Related Specifications:**
- [../../REE_CORE.md](../../REE_CORE.md) § "E3 (Trajectory Selector and Control Plane)"
- [../../architecture/precision_control.md](../../architecture/precision_control.md) — Detailed precision mechanics
- [../../architecture/control_plane_signal_map.md](../../architecture/control_plane_signal_map.md) — Signal routing
- [../../architecture/serotonin.md](../../architecture/serotonin.md) — Serotonin as anti-collapse regulator
- [../../mode_manager.md](../../mode_manager.md) — Mode specification (M1/M2/M3)
- [e3.md](e3.md) — E3 commitment and control
- [l_space.md](l_space.md) — Depth-specific precision targets
