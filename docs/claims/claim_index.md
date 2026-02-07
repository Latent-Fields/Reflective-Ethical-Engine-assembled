# REE Claim Index

This document provides a human-readable index of all typed claims in the REE architecture.

For the machine-readable version with full metadata, see [claims.yaml](claims.yaml).

---

## Invariants (INV)

Invariants are non-negotiable architectural commitments that define REE identity. Changing an invariant invalidates large parts of the project.

### Core Thesis Invariants

- **INV-001** | ethics.emergence | No Explicit Ethics Module  
  REE does not add an explicit moral objective, moral reward, or ethical scoring function. Ethics emerges from base learning dynamics plus self-other representational symmetry.  
  → [invariants.md](../invariants.md#inv-001-no-explicit-ethics-module)

- **INV-002** | coherence.definition | Coherence Includes Temporal Binding  
  Coherence includes temporal/phase compatibility, not just static metrics. Higher-degree representations bind when representational traffic is temporally compatible.  
  → [invariants.md](../invariants.md#inv-002-coherence-includes-temporal-binding)

- **INV-003** | language.emergence | Language Is Functional Self-Representation  
  Language emerges as functional self-representation and joint attention abstraction. It is not bolted on.  
  → [invariants.md](../invariants.md#inv-003-language-is-functional-self-representation)

### Architectural Safety Invariants

- **INV-004** | ethics.persistence | Ethical Cost Is Persistent  
  Ethical cost is persistent, not resettable.  
  → [invariants.md](../invariants.md#inv-004-ethical-cost-is-persistent)

- **INV-005** | ethics.mechanism | Harm Via Mirror Modeling  
  Harm to others contributes to ethical cost via mirror modelling, not symbolic rules.  
  → [invariants.md](../invariants.md#inv-005-harm-via-mirror-modeling)

- **INV-006** | residue.persistence | Residue Cannot Be Erased  
  Moral residue cannot be erased, only integrated and contextualised.  
  → [invariants.md](../invariants.md#inv-006-residue-cannot-be-erased)

- **INV-007** | language.constraint | Language Cannot Override Harm  
  Language cannot override embodied harm sensing.  
  → [invariants.md](../invariants.md#inv-007-language-cannot-override-harm)

### Control and Attention Invariants

- **INV-008** | precision.routing | Precision Is Routed and Depth-Specific  
  Precision is routed and depth-specific, not global.  
  → [invariants.md](../invariants.md#inv-008-precision-is-routed-and-depth-specific)

- **INV-009** | attention.mechanism | Attention Via Precision Modulation  
  Attention is realised through precision modulation, not symbolic control or content injection.  
  → [invariants.md](../invariants.md#inv-009-attention-via-precision-modulation)

### Operating Mode Invariants

- **INV-010** | sleep.necessity | Offline Integration Required  
  Offline integration exists and is required for long-term viability.  
  → [invariants.md](../invariants.md#inv-010-offline-integration-required)

- **INV-011** | default_mode.safety | Imagination Without Belief Update  
  Imagination and counterfactual simulation must be possible without belief update.  
  → [invariants.md](../invariants.md#inv-011-imagination-without-belief-update)

- **INV-012** | commitment.epistemology | Commitment Gates Responsibility  
  Belief and responsibility arise only through commitment to action, not mere prediction.  
  → [invariants.md](../invariants.md#inv-012-commitment-gates-responsibility)

### Foundational Invariants

- **INV-013** | cognition.structure | Cognition Is Predictive, Iterative, Multi-Timescale  
  Cognition is predictive, iterative, and multi-timescale.  
  → [invariants.md](../invariants.md#inv-013-cognition-is-predictive-iterative-multi-timescale)

- **INV-014** | architecture.separation | Separation of Representation and Regulation  
  There is a strict separation between representation (content) and regulation (control).  
  → [invariants.md](../invariants.md#inv-014-separation-of-representation-and-regulation)

- **INV-015** | ethics.emergence_mechanism | Ethics Emerges from Constraint  
  Ethics emerges from constraint, not optimisation.  
  → [invariants.md](../invariants.md#inv-015-ethics-emerges-from-constraint)

- **INV-016** | design.priority | Stability Over Performance  
  Stability, not maximal performance, is the primary viability criterion.  
  → [invariants.md](../invariants.md#inv-016-stability-over-performance)

- **INV-017** | failure.classification | Runaway Is Control Failure  
  Runaway behaviour is a control failure, not a representational one.  
  → [invariants.md](../invariants.md#inv-017-runaway-is-control-failure)

---

## Architectural Commitments (ARC)

Architectural commitments define the buildable structure. They evolve at medium speed when hypotheses stabilize.

### Core Components

- **ARC-001** | E1.role | E1 Is Persistent Predictive Substrate  
  E1 maintains deep world and self models over long horizons.  
  → [e1.md](../architecture/e1.md#1-architectural-role)

- **ARC-002** | E2.role | E2 Is Fast Forward Predictor  
  E2 generates near-future affordances and sensory predictions.  
  → [e2.md](../architecture/e2.md#1-architectural-role)

- **ARC-003** | E3.role | E3 Selects and Commits Trajectories  
  E3 gates commitment and constructs the present conditionally.  
  → [e3.md](../architecture/e3.md#1-architectural-role)

### Latent and Control Structures

- **ARC-004** | L_space.structure | L-space Is Multi-Timescale Latent Stack  
  L-space stratifies predictions by temporal depth.  
  → [l_space.md](../architecture/l_space.md#minimal-implementation-interface)

- **ARC-005** | control_plane.function | Control Plane Modulates System Operation  
  Control plane regulates precision, gain, and operating modes.  
  → [control_plane.md](../architecture/control_plane.md#role-in-ree)

- **ARC-006** | residue.geometry | Residue Is Persistent Latent Curvature  
  Residue stored as geometry makes ethical cost path-dependent.  
  → [residue_geometry.md](../architecture/residue_geometry.md#why-geometry)

### Operating Modes and Memory

- **ARC-007** | default_mode.function | Default Mode Enables Safe Imagination  
  Default Mode implements imagination via suppressed E3 and reduced sensory precision.  
  → [default_mode.md](../architecture/default_mode.md#role-in-ree)

- **ARC-008** | hippocampal_braid.function | Hippocampal Braid Stores Path Memory  
  Hippocampal braid stores and replays trajectories through latent space.  
  → [hippocampal_braid.md](../architecture/hippocampal_braid.md#role-in-ree)

### Entity Representation

- **ARC-009** | entities.emergence | Entities Emerge as Bindable Structures (Provisional)  
  Entities are sparse, persistent structures within L-space that enable error ownership.  
  → [entities_and_binding.md](../architecture/entities_and_binding.md#architectural-commitment)

---

## Mechanism Hypotheses (MECH)

Mechanism hypotheses are testable proposals that may overlap, conflict, or evolve. They iterate fast.

- **MECH-001** | phase_compatibility.binding | Phase Compatibility Implements Binding (Candidate)  
  Oscillatory phase can gate cross-horizon coordination without allowing regime overwrite.  
  → [depth_phase_spec.md](../../architecture/depth_phase_spec.md)

- **MECH-002** | tau_scoped_precision | Precision Must Be τ-Scoped (Candidate)  
  Precision requires explicit τ-scoping to prevent pathological coupling between depths.  
  → [precision_scoping.md](../../architecture/precision_scoping.md)

---

## Open Questions (OQ)

Open questions are unresolved design issues requiring further investigation.

_(No open questions formally documented yet)_

---

## Implementation Notes (IMPL)

Implementation notes provide specific guidance for instantiation.

_(Implementation notes are embedded in architecture documents rather than tracked as separate claims)_

---

## Dependency Graph (Summary)

### Invariants with No Dependencies (Axiomatic)
- INV-001, INV-002, INV-003, INV-004, INV-008, INV-010, INV-011, INV-012, INV-013, INV-014, INV-016

### Invariants Depending on Other Invariants
- INV-005 → INV-001
- INV-006 → INV-004
- INV-007 → INV-003
- INV-009 → INV-008
- INV-015 → INV-001, INV-005
- INV-017 → INV-014

### Architectural Commitments Depending on Invariants
- ARC-001 → INV-013
- ARC-002 → INV-013, ARC-001
- ARC-003 → INV-012, ARC-001, ARC-002
- ARC-004 → INV-013, INV-002
- ARC-005 → INV-008, INV-009, INV-014
- ARC-006 → INV-006, INV-004, ARC-004
- ARC-007 → INV-011, ARC-003, ARC-005
- ARC-008 → ARC-006, ARC-004
- ARC-009 → ARC-004, INV-002

### Mechanism Hypotheses Depending on Architecture
- MECH-001 → INV-002, ARC-004
- MECH-002 → INV-008, ARC-004

---

## Notes

- **Total Claims:** 28 (17 invariants, 9 architectural commitments, 2 mechanism hypotheses)
- **Conflicts Detected:** None currently documented
- **Provisional/Candidate Claims:** ARC-009, MECH-001, MECH-002

For conflict documentation, see [conflicts/](../conflicts/).
