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
