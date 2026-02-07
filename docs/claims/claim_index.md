# REE Claims Index

**Last Updated:** 2026-02-07

> This index lists all typed claims in the REE architecture. Claims are categorized by type and referenced throughout the canonical documentation.

## Claim Classification System

- **INV (Invariant):** Non-negotiable constraint; violating this changes REE identity
- **ARCH (Architectural Commitment):** Strong design choice that could theoretically vary
- **MECH (Mechanism Hypothesis):** Testable prediction about how the system works
- **OPEN (Open Question):** Unresolved issue requiring further research
- **IMPL (Implementation Note):** Practical guidance for builders

---

## Invariants (INV)

### Core Fundamental Claims

#### INV-fundamental-1: No Ethics Module
**Statement:** Ethics emerges from base learning dynamics plus representational symmetry (self↔other mapping), not from explicit moral scoring.

**Location:** [../README.md](../README.md) § "The Non-Negotiables"  
**Canonical Reference:** [../invariants.md](../invariants.md) § 1  
**Status:** stable

---

#### INV-fundamental-2: Coherence Is Temporal Binding
**Statement:** Coherence is partly a timing/phase compatibility problem, not just static consistency.

**Location:** [../README.md](../README.md) § "The Non-Negotiables"  
**Canonical Reference:** [../invariants.md](../invariants.md) § 2  
**Status:** stable

---

#### INV-fundamental-3: Language Emerges as Functional Self-Representation
**Statement:** Language emerges from multi-timescale prediction + social coupling + commitment control; it is NOT bolted-on LLM.

**Location:** [../README.md](../README.md) § "The Non-Negotiables"  
**Canonical Reference:** [../invariants.md](../invariants.md) § 3  
**Status:** stable

---

### Architectural Invariants

#### INV-001: Ethical Cost Persistence
**Statement:** Ethical cost is persistent, not resettable.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-001)  
**Depends On:** —  
**Status:** stable

---

#### INV-002: Mirror Modelling for Harm to Others
**Statement:** Harm to others contributes to ethical cost via mirror modelling, not symbolic rules.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3, § 5  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-002)  
**Depends On:** INV-fundamental-1  
**Status:** stable

---

#### INV-003: Residue Non-Erasability
**Statement:** Moral residue cannot be erased, only integrated and contextualized.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-003)  
**Depends On:** INV-001  
**Status:** stable

---

#### INV-004: Language Cannot Override Harm Sensing
**Statement:** Language cannot override embodied harm sensing.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-004)  
**Depends On:** INV-fundamental-3  
**Status:** stable

---

#### INV-005: Depth-Specific Precision Routing
**Statement:** Precision is routed and depth-specific, not global.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-005)  
**Depends On:** L-space  
**Status:** stable

---

#### INV-006: Attention as Precision Modulation
**Statement:** Attention is realized through precision modulation, not symbolic control or content injection.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-006)  
**Depends On:** INV-005  
**Status:** stable

---

#### INV-007: Offline Integration Requirement
**Statement:** Offline integration exists and is required for long-term viability.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3, § 2 step 8  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-007)  
**Depends On:** —  
**Status:** stable

---

#### INV-008: Imagination Without Belief Update
**Statement:** Imagination and counterfactual simulation must be possible without belief update.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-008)  
**Depends On:** E3 commitment gating  
**Status:** stable

---

#### INV-009: Commitment-Gated Responsibility
**Statement:** Belief and responsibility arise only through commitment to action, not mere prediction.

**Location:** [../REE_CORE.md](../REE_CORE.md) § 3, § 2 step 5  
**Canonical Reference:** [../invariants.md](../invariants.md#inv-009)  
**Depends On:** E3 commitment mechanism  
**Status:** stable

---

## Architectural Commitments (ARCH)

#### ARCH-001: Multi-Timescale Prediction Architecture
**Statement:** REE requires multiple predictive timescales (E1 for long-horizon, E2 for short-horizon).

**Location:** [architecture/e1.md](architecture/e1.md), [architecture/e2.md](architecture/e2.md)  
**Depends On:** INV-002, INV-008  
**Status:** stable

---

#### ARCH-002: Trajectory Selection Over Action Selection
**Statement:** E3 selects trajectories (paths through time), not instantaneous actions.

**Location:** [architecture/e3.md](architecture/e3.md)  
**Depends On:** INV-009, L-space  
**Status:** stable

---

#### ARCH-003: Residue as Geometric Field
**Statement:** Moral residue is represented as persistent geometric deformation φ(z) of latent space.

**Location:** [../architecture/residue_geometry.md](../architecture/residue_geometry.md)  
**Depends On:** INV-003, L-space  
**Status:** stable

---

#### ARCH-004: Depth-Stratified Latent Space
**Statement:** L-space is stratified by temporal depth (γ, β, θ, δ), not sensory modality.

**Location:** [architecture/l_space.md](architecture/l_space.md)  
**Depends On:** INV-005  
**Status:** stable

---

#### ARCH-005: Self-Model Reuse for Other-Modelling
**Statement:** Other agents are represented by reusing self-model architecture with modified coupling.

**Location:** [../architecture/social/mirror_modelling.md](../architecture/social/mirror_modelling.md)  
**Depends On:** INV-002, INV-fundamental-1  
**Status:** stable

---

#### ARCH-006: Language as Emergent Coordination Layer
**Statement:** Language emerges from predictive architecture, not as external interface.

**Location:** [../architecture/language/](../architecture/language/)  
**Depends On:** INV-fundamental-3  
**Status:** stable

---

#### ARCH-007: Sleep as Mandatory Offline Integration
**Statement:** Sleep-like offline processes are architecturally required, not optional optimization.

**Location:** [../architecture/sleep/](../architecture/sleep/)  
**Depends On:** INV-007  
**Status:** stable

---

#### ARCH-008: Mode-Dependent Control Parameter Sets
**Statement:** Different operating modes (task-engaged, default, sleep) require different control plane parameter sets.

**Location:** [architecture/control_plane.md](architecture/control_plane.md)  
**Depends On:** INV-005, INV-007, INV-008  
**Status:** stable

---

## Mechanism Hypotheses (MECH)

#### MECH-001: E1 Provides Priors to E2
**Statement:** E1's deep predictions shape E2's affordance generation via prior distributions.

**Location:** [architecture/e1.md](architecture/e1.md), [architecture/e2.md](architecture/e2.md)  
**Testable:** Yes — measure E2 performance with/without E1 priors  
**Status:** provisional

---

#### MECH-002: E1 Deep Coherence Enables Persistent Self-Model
**Statement:** E1's slow update rate and deep structure enable continuity of self across time.

**Location:** [architecture/e1.md](architecture/e1.md)  
**Testable:** Yes — measure identity persistence under E1 disruption  
**Status:** provisional

---

#### MECH-003: E2 Generates Affordance Manifold from E1 Priors
**Statement:** E2 uses E1 context to generate structured action possibilities.

**Location:** [architecture/e2.md](architecture/e2.md)  
**Testable:** Yes — compare affordance diversity with/without E1  
**Status:** provisional

---

#### MECH-004: E2 Must Remain Perceptually Corrigible
**Statement:** E2 predictions update against sensory error rather than enforcing top-down beliefs.

**Location:** [architecture/e2.md](architecture/e2.md)  
**Testable:** Yes — measure E2 response to unexpected sensory input  
**Status:** provisional

---

#### MECH-005: Default Mode Suppresses Commitment for Safe Exploration
**Statement:** Reduced E3 commitment threshold in default mode enables imagination without belief update.

**Location:** [architecture/e3.md](architecture/e3.md), [../architecture/Default_mode.md](../architecture/Default_mode.md)  
**Testable:** Yes — verify belief update disabled in default mode  
**Status:** provisional

---

#### MECH-006: Commitment Enables Belief Update
**Statement:** Only after E3 commits a trajectory do prediction errors trigger learning.

**Location:** [architecture/e3.md](architecture/e3.md)  
**Testable:** Yes — verify no learning from uncommitted rollouts  
**Status:** provisional

---

#### MECH-007: Residue Field Biases Trajectory Selection
**Statement:** Regions of latent space with high φ(z) are avoided by E3 during trajectory selection.

**Location:** [architecture/e3.md](architecture/e3.md), [../architecture/residue_geometry.md](../architecture/residue_geometry.md)  
**Testable:** Yes — measure trajectory selection bias near high-residue regions  
**Status:** provisional

---

#### MECH-008: Residue Integration Without Erasure
**Statement:** Sleep consolidation integrates residue context without reducing φ(z) magnitude.

**Location:** [../architecture/sleep/residue_integration.md](../architecture/sleep/residue_integration.md)  
**Testable:** Yes — verify φ(z) persistence post-sleep  
**Status:** provisional

---

#### MECH-009: Temporal Displacement Enables Commitment Gating
**Statement:** Representing predictions as temporally displaced allows commitment to be conditional.

**Location:** [architecture/l_space.md](architecture/l_space.md), [architecture/e3.md](architecture/e3.md)  
**Testable:** Yes — compare with non-displaced representation  
**Status:** provisional

---

#### MECH-010: Depth-Specific Precision Enables Fine-Grained Attention
**Statement:** Independent α_k per depth allows selective attention at different temporal scales.

**Location:** [architecture/control_plane.md](architecture/control_plane.md), [architecture/l_space.md](architecture/l_space.md)  
**Testable:** Yes — measure attention effects at different depths  
**Status:** provisional

---

#### MECH-011: Precision Modulation Implements Attention
**Statement:** Attention is mechanistically implemented by modulating prediction error weights (precision/gain).

**Location:** [architecture/control_plane.md](architecture/control_plane.md)  
**Testable:** Yes — verify attention effects via precision manipulation  
**Status:** provisional

---

#### MECH-020: Phase-Locking Enables Commitment
**Statement:** E3 commitment phase-aligns multi-depth predictions with motor timing.

**Location:** [architecture/entities_and_binding.md](architecture/entities_and_binding.md), [architecture/e3.md](architecture/e3.md)  
**Testable:** Yes — measure temporal alignment pre/post commitment  
**Status:** provisional

---

#### MECH-021: Hippocampal Braid Preserves Path Identity
**Statement:** Episodic memory of experienced paths preserves identity and autobiographical continuity.

**Location:** [architecture/entities_and_binding.md](architecture/entities_and_binding.md)  
**Testable:** Yes — measure identity persistence with/without path memory  
**Status:** provisional

---

## Open Questions (OPEN)

#### OPEN-002: Should "Columns" Be Formalized?
**Question:** Should "columns" be formalized as an explicit architectural concept, or remain implicit in depth stratification?

**Context:** Currently implicit in γ/β/θ/δ structure  
**Location:** [glossary.md](glossary.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-003: Minimal Architectural Features for Mirror Modelling
**Question:** What minimal architectural features are sufficient to instantiate mirror modelling?

**Context:** Required for INV-002 compliance  
**Location:** [../invariants.md](../invariants.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-004: Minimal Number of L-Space Depths
**Question:** What is the minimal number of depths required for REE compliance?

**Context:** Current specification uses four (γ, β, θ, δ)  
**Location:** [architecture/l_space.md](architecture/l_space.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-005: Binding Without Explicit Oscillations
**Question:** Can temporal binding constraints be implemented efficiently in non-neural substrates without explicit oscillations?

**Context:** Related to INV-fundamental-2  
**Location:** [../invariants.md](../invariants.md), [architecture/entities_and_binding.md](architecture/entities_and_binding.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-006: Minimal Control Channel Set
**Question:** What is the minimal set of control channels for REE compliance?

**Context:** Current specification uses 5 functional channels (dopamine-like, acetylcholine-like, serotonin-like, noradrenaline-like, histamine-like)  
**Location:** [architecture/control_plane.md](architecture/control_plane.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-007: Canonical Neuromodulator Terminology
**Question:** What is the canonical term for neuromodulator analogs?

**Context:** Current usage varies: "control signals", "neuromodulator analogs", "functional channels"  
**Location:** [glossary.md](glossary.md) "Open Questions"  
**Status:** unresolved  
**Current Preference:** "precision control signals" with "neuromodulator analog" in parentheses

---

#### OPEN-008: Minimum Sleep/Offline Integration Frequency
**Question:** What is the minimum viable sleep/offline integration frequency?

**Context:** Required by INV-007  
**Location:** [../invariants.md](../invariants.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-010: Minimal E1 Model Capacity for Identity Continuity
**Question:** What minimal model capacity is required for E1 to support identity continuity?

**Location:** [architecture/e1.md](architecture/e1.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-011: Minimal Trajectory Evaluation Horizon
**Question:** What is the minimal horizon H for ethical trajectory evaluation?

**Location:** [architecture/e3.md](architecture/e3.md) "Open Questions"  
**Status:** unresolved

---

#### OPEN-012: Objectness vs Entity Binding
**Question:** What is the relationship between entity binding (REE) and objectness in traditional cognitive architectures?

**Location:** [architecture/entities_and_binding.md](architecture/entities_and_binding.md) "Open Questions"  
**Status:** unresolved

---

## Implementation Notes (IMPL)

*(Implementation notes are scattered throughout canonical docs; this section will be expanded as more implementation guidance is consolidated)*

#### IMPL-015: E1 Update Rate Relative to E2
**Note:** E1 should update significantly slower than E2; exact ratio depends on environment dynamics.

**Location:** [architecture/e1.md](architecture/e1.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-020: E2 Prediction Horizon
**Note:** E2 horizon should cover immediate action consequences (~100ms to 2 seconds depending on embodiment).

**Location:** [architecture/e2.md](architecture/e2.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-025: E2 with Feedforward Architectures
**Note:** Pure feedforward E2 implementations may work for simple environments but may lack flexibility.

**Location:** [architecture/e2.md](architecture/e2.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-030: Equal-Cost Trajectory Handling
**Note:** When multiple trajectories have equal composite cost, tie-breaking should consider epistemic value and exploration bonus.

**Location:** [architecture/e3.md](architecture/e3.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-035: Cross-Modal Binding Conflicts
**Note:** z_γ should handle cross-modal conflicts via precision-weighted integration, not hard arbitration.

**Location:** [architecture/l_space.md](architecture/l_space.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-040: Control Plane Parameter Initialization
**Note:** Control plane parameters should be initialized conservatively (balanced precision, moderate commitment threshold).

**Location:** [architecture/control_plane.md](architecture/control_plane.md) "Open Questions"  
**Status:** guidance

---

#### IMPL-045: Binding Failure Detection
**Note:** Binding failures can be detected via coherence cost spikes across depths.

**Location:** [architecture/entities_and_binding.md](architecture/entities_and_binding.md) "Open Questions"  
**Status:** guidance

---

## Claim Dependencies Graph (Summary)

```
INV-fundamental-1 (No ethics module)
  ├─> INV-002 (Mirror modelling)
  └─> ARCH-005 (Self-model reuse)

INV-fundamental-2 (Coherence is temporal binding)
  ├─> ARCH-004 (Depth-stratified L-space)
  └─> MECH-020 (Phase-locking)

INV-fundamental-3 (Language emerges)
  ├─> INV-004 (Language can't override harm)
  └─> ARCH-006 (Language as coordination layer)

INV-005 (Depth-specific precision)
  ├─> INV-006 (Attention as precision)
  ├─> ARCH-004 (L-space stratification)
  └─> ARCH-008 (Mode-dependent control)

INV-009 (Commitment-gated responsibility)
  ├─> ARCH-002 (Trajectory selection)
  ├─> MECH-006 (Commitment enables learning)
  └─> MECH-009 (Temporal displacement)
```

---

## How to Use This Index

1. **Finding claims:** Use Ctrl+F to search by claim ID (e.g., "INV-002") or keyword
2. **Understanding dependencies:** Check "Depends On" to see prerequisite claims
3. **Locating details:** Follow "Canonical Reference" link for full elaboration
4. **Cross-referencing:** Claims reference each other; follow links to build understanding

---

## Maintenance

When adding new claims:
1. Assign claim ID following schema (INV/ARCH/MECH/OPEN/IMPL-XXX)
2. Add entry to this index
3. Add corresponding entry to claims.yaml
4. Update dependency graph if needed
5. Update changelog.md

---

## See Also

- [claims.yaml](claims.yaml) — Machine-readable claim registry
- [../invariants.md](../invariants.md) — Detailed invariant descriptions
- [../glossary.md](../glossary.md) — Term definitions
- [../changelog.md](../changelog.md) — Documentation change history
