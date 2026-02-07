# Entities and Binding — Coherence, Temporal Alignment, and Object Representation

**Claim Type:** mechanism_hypothesis  
**Scope:** entities  
**Depends On:** [INV-fundamental-2](../invariants.md#2-coherence-is-temporal-binding-not-just-static-alignment), L-space  
**Status:** provisional

---

> Coherence in REE is not just static consistency — it includes temporal/phase compatibility. Entities and object representations bind when their timing and phase relationships are compatible.

**Source:** This consolidates binding concepts from:
- [../../architecture/Hippocampal_braid.md](../../architecture/Hippocampal_braid.md) — Path memory and temporal binding
- [../../architecture/depth_phase_spec.md](../../architecture/depth_phase_spec.md) — Temporal and representational depth
- [../../architecture/latent_stack.md](../../architecture/latent_stack.md) — γ-layer sensory binding
- [../../architecture/why_attention_must_be_fragmented.md](../../architecture/why_attention_must_be_fragmented.md) — Multi-depth coherence

---

## Summary

**Central Claim:** Coherence is temporal binding, not just probabilistic consistency.

Entities (objects, agents, events) are represented as phase-compatible alignments of multi-depth predictions. Binding occurs when representational traffic at different temporal scales is temporally compatible.

---

## 1. What Is an Entity in REE?

An entity is not a static symbol or isolated feature vector.

**An entity is a stable binding pattern across multiple depths of L-space that persists through temporal displacement.**

### Components of Entity Representation
- **Sensory features (z_γ):** immediate perceptual properties
- **Affordances (z_β):** what can be done with/to the entity
- **Narrative context (z_θ):** how the entity fits into ongoing sequences
- **Regime relevance (z_δ):** why the entity matters (value, threat, attachment)

**All four depths must be phase-compatible for stable entity representation.**

**See:** [l_space.md](l_space.md) for depth definitions

---

## 2. Binding Mechanism

### Sensory Binding (γ-layer)
Primary binding occurs at z_γ (sensory binding layer).

**Function:** Fuse multi-modal evidence into coherent object representations

**Mechanism:**
- Feature conjunction across modalities (vision, touch, audition, etc.)
- Precision-weighted integration
- Phase-compatible alignment of prediction errors

**Related Claims:** [INV-006](../invariants.md#inv-006) — Attention as precision modulation

---

### Cross-Depth Coherence
Binding is not complete at z_γ alone.

**For an entity to be "real" (stable, actionable, memorable):**
- z_γ must represent its sensory features
- z_β must represent its affordances
- z_θ must represent its sequential context
- z_δ must represent its motivational relevance

**And all four must be temporally compatible.**

---

## 3. Temporal Compatibility and Phase-Locking

### The Depth-Phase Coordinate System

REE computations are defined over three orthogonal coordinates:

1. **Temporal depth (τ-depth):** prediction horizon
2. **Representational depth (ρ-depth):** abstraction height in latent stack
3. **Phase (φ):** routing, binding, and commitment eligibility regime

**A REE state is well-formed only when tagged with all three:**

```
REE Token := ⟨z | τ, ρ, φ, π⟩

Where:
- z = latent content
- τ = temporal depth (γ, β, θ, δ)
- ρ = representational depth (shallow/mid/deep)
- φ = phase / control mode
- π = precision (confidence / gain)
```

**Source:** [../../architecture/depth_phase_spec.md](../../architecture/depth_phase_spec.md)

---

### Architectural Invariant: No Cross-Band Mixing

**Predictions, errors, and confidence must not be mixed across τ bands without an explicit projection or aggregation operator.**

This constraint prevents:
- Fast sensory predictions from being overwritten by slow regime priors
- Deep abstractions from masquerading as high-certainty sensory states

**Related Claims:** [INV-006](../invariants.md#inv-006) — Perceptual corrigibility

---

### Phase-Locking for Commitment

When E3 commits a trajectory, it **phase-aligns** predictions across depths with motor execution timing.

**Effect:** The temporally displaced bundle collapses into a unitary present ("now").

**See:** [e3.md](e3.md) § 6 "Commitment and Temporal Collapse"

---

## 4. The Hippocampal Braid: Path Memory and Identity

### Role
The hippocampal braid is responsible for **path memory**: the indexing, storage, and replay of experienced trajectories through latent space.

It does NOT:
- compute value
- select actions
- overwrite perception
- flatten or optimise ethical residue

**Its function is orthogonal to valuation and control.**  
It exists to preserve identity, continuity, and reflectability over time.

**Source:** [../../architecture/Hippocampal_braid.md](../../architecture/Hippocampal_braid.md)

---

### Field vs Path Distinction

REE distinguishes between two mathematical objects:

#### Residue Field
A persistent curvature over latent space: **φ(z)**  
Encodes ethical cost and moral residue.

**See:** [../../architecture/residue_geometry.md](../../architecture/residue_geometry.md)

---

#### Paths Through the Field
Time-ordered trajectories: **γ(t) = z(t), t ∈ [t₀, t₁]**

**Ethics is encoded in the field.**  
**Identity and autobiographical memory arise from the paths.**

The hippocampal braid operates exclusively on paths.

---

### Episodic Traces

The hippocampal braid stores **indexed trajectories**, not isolated states.

A minimal episodic trace:

```
Γᵢ = {
  z(t),      // latent state (z_S and z_A)
  a(t),      // committed action
  Δφ,        // experienced ethical curvature
  c(t),      // contextual / salience annotations
  t          // temporal ordering
}_{t₀}^{t₁}
```

These traces encode **experienced traversal**, not evaluation.

---

### Event Segmentation

Continuous trajectories γ(t) are segmented into **events** at points of:
- Action commitment (E3 collapse)
- Sharp changes in prediction error or precision
- Contextual or motivational shifts

**Function:** Prevent memory from becoming undifferentiated stream  
**Supports:** Recall, replay, and narrative recomposition

---

## 5. Why Attention Must Be Fragmented

**Claim:** Stable multi-depth coherence requires selective attention.

Global coherence across all depths simultaneously is computationally intractable and would prevent flexible cognition.

**Attention (implemented as depth-specific precision modulation) allows:**
- Selective binding of relevant features
- Suppression of irrelevant dimensions
- Flexible switching between entity representations

**Source:** [../../architecture/why_attention_must_be_fragmented.md](../../architecture/why_attention_must_be_fragmented.md)

**Related Claims:** [INV-006](../invariants.md#inv-006) — Attention as precision modulation

---

## 6. Binding and Other-Modelling

**Mirror modelling** (representing other agents) reuses the same binding architecture:

Other agents are represented as:
- Phase-compatible multi-depth predictions
- Using the same z_γ/z_β/z_θ/z_δ structure
- But with modified coupling and no interoceptive closure

**This architectural symmetry enables embodied understanding of others.**

**See:** [../../architecture/social/mirror_modelling.md](../../architecture/social/mirror_modelling.md)

**Related Claims:** [INV-002](../invariants.md#inv-002) — Mirror modelling for harm to others

---

## Summary Statement

Entities in REE are not symbols or feature vectors — they are **phase-compatible binding patterns** across temporal depths.

Binding requires:
- Sensory fusion at z_γ
- Cross-depth coherence across z_γ, z_β, z_θ, z_δ
- Temporal/phase compatibility
- Precision-gated attention

**Coherence is not static consistency — it is temporal binding.**

---

## Open Questions

- What minimal phase-locking precision is required for stable entity binding? *(MECH-050)*
- Can binding occur without explicit oscillatory mechanisms? *(OPEN-005)*
- How are binding failures (fragmentation) detected and corrected? *(IMPL-045)*
- What is the relationship between entity binding and objectness in traditional cognitive architectures? *(OPEN-012)*

---

## Related Claims

- **INV-fundamental-2:** Coherence is temporal binding — this document elaborates the mechanism
- **INV-005:** Depth-specific precision routing — enables selective binding
- **INV-006:** Attention as precision modulation — implements binding control
- **MECH-020:** Phase-locking enables commitment
- **MECH-021:** Hippocampal braid preserves path identity

---

## References / Source Fragments

**Primary Sources:**
- [../../architecture/Hippocampal_braid.md](../../architecture/Hippocampal_braid.md) — Path memory mechanism
- [../../architecture/depth_phase_spec.md](../../architecture/depth_phase_spec.md) — Temporal/representational/phase coordinates
- [../../architecture/latent_stack.md](../../architecture/latent_stack.md) — Depth stratification
- [../../architecture/why_attention_must_be_fragmented.md](../../architecture/why_attention_must_be_fragmented.md) — Attention necessity

**Related Specifications:**
- [l_space.md](l_space.md) — Latent depth definitions
- [e3.md](e3.md) — Commitment and phase-locking
- [control_plane.md](control_plane.md) — Precision control
- [../../architecture/social/mirror_modelling.md](../../architecture/social/mirror_modelling.md) — Other-agent binding
