# REE Documentation Map

> **Entry Point for Reflective-Ethical Engine Documentation**

This documentation tree provides a structured, navigable guide to the Reflective-Ethical Engine (REE) architecture. All content is preserved from the original documentation, reorganized for clarity and single-source-of-truth canonical references.

## Quick Navigation

### Start Here
- **First-time readers:** Begin with [../README.md](../README.md) (repository root) for the three non-negotiable claims
- **Implementation teams:** Go to [REE_MIN_SPEC.md](REE_MIN_SPEC.md) for minimal requirements
- **Architecture overview:** Read [REE_overview.md](REE_overview.md) for high-level introduction

### Core Specification
- [**Invariants**](invariants.md) — Non-negotiable architectural constraints that define REE identity
- [**Glossary**](glossary.md) — Canonical terms and definitions with anchors
- [**Claims Index**](claims/claim_index.md) — Typed claims registry (invariants, commitments, hypotheses)

### Canonical Architecture Components

All architecture components have a single canonical definition source. Other references link here.

- [**E1 (Deep Predictor)**](architecture/e1.md) — Long-horizon context model
- [**E2 (Fast Predictor)**](architecture/e2.md) — Short-horizon affordance engine
- [**E3 (Trajectory Selector)**](architecture/e3.md) — Commitment and control plane
- [**L-Space (Latent Stack)**](architecture/l_space.md) — Multi-depth stratified latent space (γ, β, θ, δ)
- [**Control Plane**](architecture/control_plane.md) — Precision, gain, and regulatory control
- [**Entities and Binding**](architecture/entities_and_binding.md) — Object representation and temporal coherence

### Specialized Subsystems

These elaborate specific REE capabilities. See [../architecture/](../architecture/) for full content.

- **Sleep & Offline Integration:** [../architecture/sleep/](../architecture/sleep/)
- **Language Emergence:** [../architecture/language/](../architecture/language/)
- **Social Cognition:** [../architecture/social/](../architecture/social/)
- **Regulatory Biology:** [astrocyte_aware_regulatory_stack/](astrocyte_aware_regulatory_stack/)

### Additional Resources
- [**Failure Modes**](REE_failure_modes.md) — Predicted pathologies and their mechanisms
- [**Changelog**](changelog.md) — Documentation reorganization history
- [**Archive**](archive/) — Preserved legacy content and migrated sections

## Documentation Organization Principles

This documentation follows a **dependency-aware refactoring** approach:

1. **Single Source of Truth:** Each concept has ONE canonical definition file
2. **Lift and Shift:** Original content is preserved intact; links replace duplicates
3. **Typed Claims:** Each major section declares its claim type (invariant, commitment, hypothesis, etc.)
4. **Stable Navigation:** Old paths have redirect stubs; all links are maintained

## Claim Classification

REE documentation uses a typed-claims system to distinguish:

- **Invariant:** Non-negotiable constraint; violating this changes REE's identity
- **Architectural Commitment:** Strong design choice that could theoretically vary
- **Mechanism Hypothesis:** Testable prediction about how the system works
- **Open Question:** Unresolved issue requiring further research
- **Implementation Note:** Practical guidance for builders

See [claims/claim_index.md](claims/claim_index.md) for the complete registry.

## How to Navigate This Documentation

```
Start: README.md (you are here)
  ├─> For Theory: Read invariants.md, then architecture/
  ├─> For Building: Read REE_MIN_SPEC.md, then ../architecture/
  ├─> For Context: Read glossary.md, then ../REE_CORE.md
  └─> For Specifics: Use claims/ to find exact statements
```

## Relationship to Repository Root

- **Repository root README:** [../README.md](../README.md) — Entry point with three core claims
- **Canonical spine:** [../REE_CORE.md](../REE_CORE.md) — Complete minimal agent loop specification
- **This documentation tree:** Canonical references and elaborations

## Status

This documentation structure was created on 2026-02-07 as part of a systematic refactoring to improve navigability and maintain single-source-of-truth for all technical concepts.

See [changelog.md](changelog.md) for migration details.
