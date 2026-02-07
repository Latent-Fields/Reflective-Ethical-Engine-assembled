# REE Documentation Structure

This documentation has been refactored into a structured, dependency-aware system that explicitly surfaces inconsistencies and forks rather than resolving them silently.

## Navigation Guide

### Core Architecture Documents

The REE architecture is built on several foundational concepts. Each has a canonical definition location:

- **[E1 (Deep Predictor)](architecture/e1.md)** — Persistent predictive substrate; long-horizon context model
- **[E2 (Fast Predictor)](architecture/e2.md)** — Fast forward predictor; affordance and immediate inference engine
- **[E3 (Trajectory Selector)](architecture/e3.md)** — Trajectory selection and commitment engine
- **[L-space (Latent Stack)](architecture/l_space.md)** — Multi-timescale latent manifold stratified by prediction depth
- **[Control Plane](architecture/control_plane.md)** — Precision, gain, and mode regulation
- **[Entities and Binding](architecture/entities_and_binding.md)** — Entity representation and binding mechanisms
- **[Residue Geometry](architecture/residue_geometry.md)** — Persistent moral curvature over latent space
- **[Default Mode](architecture/default_mode.md)** — Internal generative mode; imagination without commitment
- **[Hippocampal Braid](architecture/hippocampal_braid.md)** — Path memory and replay

### Subsystems

- **[Sleep/Offline Integration](../architecture/sleep/)** — Replay, consolidation, and residue-preserving reprojection
- **[Language](../architecture/language/)** — Symbolic mediation constrained by harm and residue
- **[Social Cognition](../architecture/social/)** — Mirror modeling, coupling, and misalignment detection

### Foundational Documents

- **[Invariants](invariants.md)** — Non-negotiable architectural commitments that define REE identity
- **[Glossary](glossary.md)** — Canonical definitions of terms and notation

### Claims and Conflicts

- **[Claim Index](claims/claim_index.md)** — Human-readable list of all typed claims
- **[Claims Registry](claims/claims.yaml)** — Machine-readable claim database with dependencies
- **[Conflicts](conflicts/)** — Explicitly documented incompatibilities and forks

### Archive

- **[Archive](archive/)** — Superseded content preserved for historical reference

### Change Tracking

- **[Changelog](changelog.md)** — Summary of documentation refactoring and migrations

## Document Structure

Each architectural document follows a standard structure:

```
# [Component Name]

[Claim Type]: invariant | architectural_commitment | mechanism_hypothesis | open_question | implementation_note
[Scope]: [What this document covers]
[Depends On]: [List of prerequisite concepts]
[Status]: stable | provisional | legacy | candidate

[Content...]
```

## Reading Paths

### For Implementers
1. Start with [../REE_CORE.md](../REE_CORE.md) (canonical spine)
2. Read [REE_MIN_SPEC.md](REE_MIN_SPEC.md) (minimum specification)
3. Review [E1](architecture/e1.md), [E2](architecture/e2.md), [E3](architecture/e3.md) (core components)
4. Understand [L-space](architecture/l_space.md) and [Control Plane](architecture/control_plane.md)

### For Researchers
1. Start with [Invariants](invariants.md) (architectural commitments)
2. Review [Claims Index](claims/claim_index.md) (typed claims)
3. Examine [Conflicts](conflicts/) (known incompatibilities)
4. Explore architectural documents by interest

### For Contributors
1. Read [../CONTRIBUTING.md](../CONTRIBUTING.md)
2. Review [../DANIEL_README.md](../DANIEL_README.md) (refinement process)
3. Understand claim typing system
4. Check for existing claims before adding new ones

## Design Principles

This documentation structure follows specific global rules:

1. **No content deletion** — Redundant or superseded content is moved to archive/, not deleted
2. **Preserve original wording** — Prefer moving and splitting over paraphrasing
3. **Never silently change meaning** — All semantic changes are explicit
4. **Never resolve contradictions by choosing a winner** — Conflicts are represented explicitly
5. **Conservative invariants** — If invariants conflict, both are downgraded to architectural_commitment
6. **Explicit claim typing** — Every major section has a claim type
7. **Dependency tracking** — Claims specify what they depend on

## Claim Types

- **invariant** — Non-negotiable architectural commitment; changing this invalidates REE
- **architectural_commitment** — Buildable structure; medium-speed evolution
- **mechanism_hypothesis** — Testable hypothesis; may overlap or conflict; fast iteration
- **open_question** — Unresolved design question
- **implementation_note** — Specific implementation guidance

## Status Values

- **stable** — Well-established, unlikely to change
- **provisional** — Working hypothesis, may evolve
- **legacy** — Superseded but preserved for reference
- **candidate** — Under evaluation, not yet committed
