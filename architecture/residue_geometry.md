# Residue geometry

Residue is stored as persistent curvature over latent space.

## Minimal representation

- Maintain a function \(\phi(z)\) over latent space (implemented as a small neural network, radial basis functions, or a k-nearest neighbors map).
- Update \(\phi\) after executing a trajectory to increase the cost around visited latent states proportional to ethical cost.

## Why geometry

If residue were a scalar penalty, it would be easily traded off against reward and optimized away.
A spatial field \(\phi(z)\) makes residue *path dependent* and supports moral continuity.
