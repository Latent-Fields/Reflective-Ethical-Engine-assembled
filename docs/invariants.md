# REE Invariants

**Claim Type:** invariant  
**Scope:** repo  
**Status:** stable

> These are the **non-negotiable architectural constraints** that define REE identity. An implementation that violates any of these is not REE-compliant.

## Source

This document consolidates invariants from:
- [../REE_CORE.md](../REE_CORE.md) § 3 "Non-Negotiable Architectural Invariants"
- [../README.md](../README.md) § "The Non-Negotiables"

## The Three Fundamental Claims

These three claims (from repository root README) are the foundation of REE:

### 1. No "Ethics Module" or Moral Scoring Layer

**Claim:** Ethics emerges from base learning dynamics (avoid harm / seek reward) plus representational symmetry.

When other agents are represented as *self-like* in prediction and learning mechanics, care for others is not an overlay — it emerges as the same machinery applied under a self↔other mapping.

**Implication:** Adding an explicit ethics layer, moral reward, or ethical scoring function on top of action selection changes the thesis.

### 2. Coherence Is Temporal Binding, Not Just Static Alignment

**Claim:** Coherence is partly a timing/phase compatibility problem.

Higher-degree perceptual representations bind when representational traffic is temporally compatible — and hippocampus-like rollout traffic participates in that binding.

**Implication:** Reducing coherence to static consistency checks changes the thesis.

### 3. Language Emerges as Functional Self-Representation

**Claim:** Language emerges from the architecture's existing ingredients: multi-timescale prediction, shared latent substrate, social/joint attention constraints, and commitment control.

Language acts as an abstraction of joint attention and control state — it can represent the architecture itself.

**Implication:** Treating language as an external interface only (e.g., bolted-on LLM) changes the thesis.

---

## Architectural Invariants

The following invariants define what must exist in any REE-compliant implementation:

### INV-001: Ethical Cost Persistence
**Ethical cost is persistent, not resettable.**

Moral residue accumulates over time and cannot be cleared by fiat. The agent carries its ethical history.

**Related Claims:** [ARCH-003](#), [MECH-007](#)  
**Source:** REE_CORE.md § 3

---

### INV-002: Mirror Modelling for Harm to Others
**Harm to others contributes to ethical cost via mirror modelling, not symbolic rules.**

Other agents are represented using the same self-model architecture, enabling embodied understanding of harm rather than rule-based moral reasoning.

**Related Claims:** [ARCH-005](#), [MECH-015](#)  
**Source:** REE_CORE.md § 3, § 5

---

### INV-003: Residue Non-Erasability
**Moral residue cannot be erased, only integrated and contextualized.**

Residue forms persistent geometric deformation of latent space. It can be understood and worked with, but not deleted.

**Related Claims:** [ARCH-003](#), [MECH-008](#)  
**Source:** REE_CORE.md § 3

---

### INV-004: Language Cannot Override Harm Sensing
**Language cannot override embodied harm sensing.**

Linguistic/symbolic representations cannot suppress or replace direct homeostatic and interoceptive harm signals.

**Related Claims:** [ARCH-006](#), [MECH-018](#)  
**Source:** REE_CORE.md § 3

---

### INV-005: Depth-Specific Precision Routing
**Precision is routed and depth-specific, not global.**

Precision/gain control operates independently at different latent depths (γ, β, θ, δ), enabling fine-grained attention and commitment control.

**Related Claims:** [ARCH-004](#), [MECH-010](#)  
**Source:** REE_CORE.md § 3

---

### INV-006: Attention as Precision Modulation
**Attention is realized through precision modulation, not symbolic control or content injection.**

Attention alters the weighting of prediction errors rather than adding new sensory content or symbolically selecting attended items.

**Related Claims:** [ARCH-004](#), [MECH-011](#)  
**Source:** REE_CORE.md § 3

---

### INV-007: Offline Integration Requirement
**Offline integration exists and is required for long-term viability.**

REE agents must perform periodic offline consolidation (sleep-like processes) to integrate residue, recalibrate precision, and improve world models.

**Related Claims:** [ARCH-007](#), [MECH-020](#)  
**Source:** REE_CORE.md § 3, § 2 step 8

---

### INV-008: Imagination Without Belief Update
**Imagination and counterfactual simulation must be possible without belief update.**

The system must support generating hypothetical futures without committing to them or updating world models based on imagined outcomes.

**Related Claims:** [ARCH-002](#), [MECH-005](#)  
**Source:** REE_CORE.md § 3

---

### INV-009: Commitment-Gated Responsibility
**Belief and responsibility arise only through commitment to action, not mere prediction.**

Prediction errors become epistemically and ethically relevant only after the agent commits to a trajectory. Hypothetical rollouts don't trigger belief updates or residue formation.

**Related Claims:** [ARCH-002](#), [MECH-006](#)  
**Source:** REE_CORE.md § 3, § 2 step 5

---

## Derived Constraints

The following constraints are logical consequences of the above invariants:

### Multi-Timescale Prediction is Mandatory
To support both fast affordances (E2) and long-horizon consequences (E1), the architecture must maintain multiple predictive timescales.

**Derived From:** INV-002, INV-008

### Self-Model Must Support Self↔Other Mapping
The self-model architecture must be reusable for representing others with modified coupling.

**Derived From:** INV-002

### Harm Signals Must Be Persistent and Non-Overridable
Direct homeostatic/interoceptive signals must remain available regardless of symbolic or linguistic content.

**Derived From:** INV-004

---

## What Is Intentionally Left Open

REE deliberately does **not** fix:
- Model classes (can be neural networks, probabilistic models, hybrid systems)
- Planners (can use tree search, sampling, gradient-based methods)
- Embodiment level (can be simulated, robotic, purely abstract)
- Training regimes (can use RL, active inference, self-supervised learning)
- Environments (can be simple toy worlds or complex embodied scenarios)

REE constrains **what must exist**, not **how it must be built**.

---

## Violation Detection

An implementation violates REE invariants if it:
- Allows residue to be reset or cleared (violates INV-003)
- Uses symbolic moral rules instead of mirror modelling (violates INV-002)
- Implements global attention without depth-specific precision (violates INV-005, INV-006)
- Lacks offline integration/sleep (violates INV-007)
- Updates beliefs from uncommitted rollouts (violates INV-009)
- Allows language to suppress harm signals (violates INV-004)

---

## Open Questions

- What minimal architectural features are sufficient to instantiate mirror modelling? *(See OPEN-003 in claims index)*
- Can temporal binding constraints be implemented efficiently in non-neural substrates? *(See OPEN-005 in claims index)*
- What is the minimum viable sleep/offline integration frequency? *(See OPEN-008 in claims index)*

---

## Related Claims

See [claims/claim_index.md](claims/claim_index.md) for:
- All INV-* claims (invariants)
- ARCH-* claims (architectural commitments that elaborate these invariants)
- MECH-* claims (testable mechanisms that implement these invariants)

---

## References / Source Fragments

**Primary Sources:**
- [../REE_CORE.md](../REE_CORE.md) § 3 "Non-Negotiable Architectural Invariants"
- [../README.md](../README.md) § "The Non-Negotiables"

**Elaborations:**
- [architecture/control_plane.md](architecture/control_plane.md) — INV-005, INV-006 details
- [architecture/e3.md](architecture/e3.md) — INV-009 commitment mechanism
- [../architecture/sleep/](../architecture/sleep/) — INV-007 offline integration
- [../architecture/social/mirror_modelling.md](../architecture/social/mirror_modelling.md) — INV-002 details
