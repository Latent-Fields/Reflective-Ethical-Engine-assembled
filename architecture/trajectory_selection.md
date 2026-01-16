# Trajectory selection (E3)

E3 evaluates candidate futures and commits to one trajectory.

## Candidate generation

Generate \(N\) candidate trajectories \(\zeta_i\) by rolling the latent model forward for horizon \(H\).

Common options:
- Model Predictive Control (MPC) rollouts with random shooting.
- Cross-Entropy Method (CEM) sampling.
- Beam search for discrete action spaces.

## Scoring

Score each candidate with:

\[
J(\zeta)=\mathcal{F}(\zeta)+\lambda\,M(\zeta)+\rho\,\Phi_R(\zeta)
\]

## Commitment

Commitment is implemented as a precision increase at action/control depth (\(\beta\) and sometimes \(\gamma\)):

- reduce action entropy for the selected plan
- increase weighting of action-level prediction error (stabilizes execution)

This corresponds to dopamine-like commitment without requiring a reward-only interpretation.
