# Latent stack (L-space)

REE uses a multi-timescale latent stack to represent temporally displaced prediction depths.

## Minimal implementation interface

Implement each depth \(k\in\{\gamma,\beta,\theta,\delta\}\) with:

- `encode_k(o_t, prev_state)` → `z_k(t)`
- `predict_k(z_k(t))` → `z_k(t+1)`
- `topdown_kplus1_to_k(z_{k+1}(t))` → prior / conditioning signal for depth \(k\)

## Interpretation

- \(z_\gamma\): sensory binding / feature conjunction.
- \(z_\beta\): action-set maintenance and immediate control state.
- \(z_\theta\): sequence context and ordering.
- \(z_\delta\): regime, motivational set, default-mode attractor.

REE does not require explicit oscillations for v0. Oscillatory phase can be added later as a scheduling / gating mechanism.
