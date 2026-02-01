# Precision control (monoamine analogue)

REE uses depth-indexed precision gains \(\alpha_k\) to control how strongly errors at different depths shape belief and action.

## Minimal knobs

For each depth \(k\):

- `alpha_k` multiplies the prediction error term in training / inference.
- Optionally, `alpha_k` modulates sampling temperature (higher precision → lower entropy).

## Functional roles (analogue)

- Dopamine-like: increases commitment (reduced action entropy) and stabilizes selected outputs.
- Noradrenaline-like: global reset signal when unexpected uncertainty spikes.
- Acetylcholine-like: increases sensory gain (boost \(\alpha_\gamma\)).
- Serotonin-like: holds options open; slows premature collapse (limits over-commitment).

## Astrocyte-aware regulatory stack

**Note:** The above framing treats monoamines as direct control knobs. A more neuroscience-informed perspective reinterprets monoamines as **broadcast meta-regulatory signals** that bias a slower astrocytic regulatory substrate, which then modulates precision/gain/plasticity with spatial and temporal lags.

See `docs/astrocyte_aware_regulatory_stack/` for:

- Why monoamines are not direct knobs (astrocytes mediate their effects).
- How to model the slow regulatory field \(R(x,t)\) that produces \(\alpha_k(x,t)\).
- Implications for care budget, inertia, and sleep recalibration.

For REE-v0, the direct-knob model (above) is a valid simplification. Future implementations should account for the layered regulatory architecture documented in the astrocyte-aware module.
