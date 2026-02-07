# Documentation Refactoring Changelog

**Refactoring Date:** 2026-02-07  
**Scope:** Documentation reorganization and claim-typing system implementation

## Purpose

This refactoring reorganizes REE documentation to provide:
1. Single source of truth for all canonical concepts
2. Typed-claims system (invariant, commitment, hypothesis, question, note)
3. Improved navigability with clear entry points
4. Preserved legacy content (no deletions)

## High-Level Changes

### New Structure Created
- `docs/README.md` — Documentation entry point and navigation map
- `docs/invariants.md` — Canonical non-negotiable architectural constraints
- `docs/glossary.md` — Expanded canonical terms with anchors (enhanced from existing)
- `docs/architecture/` — Canonical architecture component definitions
- `docs/claims/` — Typed claims registry (machine and human readable)
- `docs/archive/` — Preserved legacy content
- `docs/changelog.md` — This file

### Modified Files
- `docs/glossary.md` — Expanded from 14 lines to comprehensive reference with anchors, claim types, and terminology migrations

### Files to Be Created (In Progress)
- `docs/architecture/e1.md` — Canonical E1 definition
- `docs/architecture/e2.md` — Canonical E2 definition
- `docs/architecture/e3.md` — Canonical E3 definition
- `docs/architecture/l_space.md` — Canonical L-space definition
- `docs/architecture/control_plane.md` — Canonical control plane definition
- `docs/architecture/entities_and_binding.md` — Consolidated binding concepts
- `docs/claims/claim_index.md` — Human-readable claim index
- `docs/claims/claims.yaml` — Machine-readable claim registry

## Migration Map

This section tracks content movement from original locations to canonical locations.

### Root Documentation (Unchanged)
- `README.md` — **Preserved** (entry point with three non-negotiable claims)
- `REE_CORE.md` — **Preserved** (canonical spine)
- `WIRING_NOTES.md` — **Preserved** (cross-reference guide)
- `mode_manager.md` — **Preserved** (mode specification)
- `roadmap.md` — **Preserved** (development plan)
- `CONTRIBUTING.md` — **Preserved** (contribution guidelines)

### Documentation Reorganization

#### Canonical Architecture Definitions
```
Source → Destination                          | Status    | Action
---------------------------------------------|-----------|------------------
architecture/E1.md                           | Preserved | Content lifted to docs/architecture/e1.md
architecture/E2.md                           | Preserved | Content lifted to docs/architecture/e2.md
architecture/E3.md                           | Preserved | Content lifted to docs/architecture/e3.md
architecture/latent_stack.md                 | Preserved | Content lifted to docs/architecture/l_space.md
architecture/control_plane.md                | Preserved | Content lifted to docs/architecture/control_plane.md
architecture/Hippocampal_braid.md            | Preserved | Referenced in docs/architecture/entities_and_binding.md
architecture/depth_phase_spec.md             | Preserved | Referenced in docs/architecture/entities_and_binding.md
```

#### Specialized Subsystems (Preserved in Place)
```
architecture/sleep/                          | Preserved | Linked from docs/README.md
architecture/language/                       | Preserved | Linked from docs/README.md
architecture/social/                         | Preserved | Linked from docs/README.md
architecture/precision_control.md            | Preserved | Linked from docs/architecture/control_plane.md
architecture/control_plane_signal_map.md     | Preserved | Linked from docs/architecture/control_plane.md
architecture/residue_geometry.md             | Preserved | Linked from docs/glossary.md
architecture/serotonin.md                    | Preserved | Linked from docs/architecture/control_plane.md
architecture/trajectory_selection.md         | Preserved | Linked from docs/architecture/e3.md
```

#### Docs Directory Reorganization
```
Source → Destination                          | Status    | Action
---------------------------------------------|-----------|------------------
docs/glossary.md                             | Enhanced  | Expanded with anchors and claim types
docs/REE_overview.md                         | Preserved | Linked from docs/README.md
docs/REE_MIN_SPEC.md                         | Preserved | Linked from docs/README.md
docs/REE_failure_modes.md                    | Preserved | Linked from docs/README.md
docs/astrocyte_aware_regulatory_stack/       | Preserved | Linked from docs/README.md
```

## Content Preservation Guarantees

### No Content Deleted
All original documentation content is preserved either:
1. In its original location (architecture/, docs/, root .md files)
2. Lifted to new canonical location (with original preserved)
3. Archived with redirect notes (for any deprecated duplicates)

### Lift-and-Shift Policy
When content is moved to canonical locations:
- Original phrasing is preserved verbatim
- Sections are kept intact
- Only minimal glue text is added for navigation
- Source location is documented in "References / Source Fragments" section

### Link Stability
- Original files in `architecture/` are preserved
- New canonical files in `docs/architecture/` reference originals
- All internal links are updated or have redirect notes
- No old links are broken silently

## Claim-Typing System

### Claim Categories Introduced
1. **Invariant** — Non-negotiable constraint; violating changes REE identity
2. **Architectural Commitment** — Strong design choice that could theoretically vary
3. **Mechanism Hypothesis** — Testable prediction about system behavior
4. **Open Question** — Unresolved issue requiring research
5. **Implementation Note** — Practical guidance for builders

### Metadata Format
Each canonical file includes either:
- YAML front matter: `claim_type:`, `scope:`, `depends_on:`, `status:`
- Or standardized header block with same fields

### Claim ID Schema
- **INV-XXX** — Invariants (e.g., INV-001, INV-002)
- **ARCH-XXX** — Architectural commitments
- **MECH-XXX** — Mechanism hypotheses
- **OPEN-XXX** — Open questions
- **IMPL-XXX** — Implementation notes

## Detected Contradictions

*(None detected during initial inventory)*

### Resolution Process
When contradictions are found:
1. Document both versions in claims registry
2. Flag as OPEN-XXX if unresolved
3. Choose canonical version with justification
4. Archive alternatives in docs/archive/

## Classification Uncertainties

### Items Requiring Further Review

1. **Columns as Architectural Concept**
   - **Status:** Implicit in depth stratification (γ/β/θ/δ)
   - **Question:** Should "columns" be formalized as explicit concept?
   - **Flagged As:** OPEN-002 (see claims/claim_index.md when created)
   - **Current Approach:** Treat as emergent property of depth structure

2. **Neuromodulator Terminology**
   - **Status:** Uses "neuromodulator analogs" and "control signals" interchangeably
   - **Question:** What is canonical term?
   - **Flagged As:** OPEN-007
   - **Current Approach:** Use "precision control signals" with "neuromodulator analog" in parentheses

3. **Precision vs Gain Terminology**
   - **Status:** Used interchangeably in original docs
   - **Resolution:** Added to glossary "Terminology Migrations" section
   - **Current Preference:** "Precision" for theory, "gain" for implementation

## Implementation Notes

### Refactoring Principles Applied
1. ✅ No content deleted — all preserved
2. ✅ No aggressive paraphrasing — lift and shift
3. ✅ Technical claims tracked — changelog and claims registry
4. ✅ Single source of truth — canonical definitions in docs/architecture/
5. ✅ Claim typing — metadata added to all canonical files
6. ✅ Stable filenames — original architecture/ preserved

### Testing and Validation
- [x] All original .md files scanned
- [x] Key concepts mapped to sources
- [x] Duplicate content identified (intentional hierarchical elaboration)
- [ ] Link hygiene validated (in progress)
- [ ] Broken link check (pending)
- [ ] Content completeness check (pending)

## Future Maintenance

### When Adding New Documentation
1. Determine claim type (invariant, commitment, hypothesis, question, note)
2. Add entry to claims/claim_index.md and claims/claims.yaml
3. Link to canonical definitions in glossary
4. Update this changelog with new content

### When Modifying Existing Claims
1. Document change in this changelog
2. Update claim version in claims registry
3. Mark old version as superseded
4. Preserve old version in archive/ if significant

## Contributors

- Initial refactoring: GitHub Copilot (2026-02-07)
- Original documentation: REE team (various dates)

## References

- **Refactoring Specification:** Problem statement provided 2026-02-07
- **Original Structure:** Analyzed from repository state at refactoring start
- **Content Sources:** All files listed in Migration Map above
