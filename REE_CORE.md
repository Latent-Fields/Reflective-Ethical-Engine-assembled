# Reflective-Ethical Engine (REE) — Core Architecture

## 1. Purpose

The Reflective-Ethical Engine (REE) is a **reference architecture for agents that act under uncertainty while retaining ethical continuity over time**.

REE addresses a specific failure mode in existing artificial agents: ethical concern is treated as a design-time constraint or reward signal that can be optimised away, reset, or exported to human oversight. In contrast, REE treats ethics as a **runtime property of agency** arising from prediction, harm sensing, memory, and persistence.

REE is **not**:
- a moral code,
- a value list,
- a normative ethical theory,
- or a single algorithm.

REE **is**:
- a constraint-complete architectural specification that any instantiation must satisfy if it is to remain ethically coherent as capability scales.

## 2. The Minimal Agent Loop (Canonical Spine)

All REE-compliant agents implement the following loop.

1. **Sense**
   - Receive multi-modal exteroceptive inputs.
   - Receive interoceptive and homeostatic state signals.
   - Receive damage / degradation signals.

2. **Update Latent State**
   - Update a temporally stratified latent stack (L-space) representing the agent’s predictive state across multiple horizons.

3. **Generate Trajectories**
   - Generate multiple candidate future trajectories ζ via internal rollouts of the world model.

4. **Score Trajectories**
   Each trajectory is scored using:
   - a **reality constraint** ℱ (predictive coherence and viability),
   - an **ethical cost** M (predicted degradation of self and others),
   - a **residue field** R (persistent deformation from past harm).

5. **Select Trajectory**
   - Select a trajectory under precision-controlled commitment.

6. **Act**
   - Execute the next action implied by the selected trajectory.

7. **Update Residue**
   - If harm or degradation occurred (actual or predicted), update persistent residue.

8. **Offline Integration (Sleep)**
   - Periodically perform offline consolidation to:
     - improve the world model,
     - integrate and contextualise residue,
     - recalibrate precision and option space.

This loop is the **only complete description of REE**.
All other documents elaborate parts of this loop.

## 3. Non-Negotiable Architectural Invariants

An implementation is **not REE-compliant** if it violates any of the following:

- Ethical cost is **persistent**, not resettable.
- Harm to others contributes to ethical cost via **mirror modelling**, not symbolic rules.
- Moral residue **cannot be erased**, only integrated and contextualised.
- Language **cannot override embodied harm sensing**.
- Precision is **routed and depth-specific**, not global.
- Offline integration exists and is required for long-term viability.

These invariants define the identity of REE.

## 4. Core Components (Summary Only)

### World Interface  
Agents sense:
- the external world (multi-modal),
- internal state (interoception, homeostasis),
- and degradation / harm signals.  

### Latent Stack (L-Space)  
Internal state is represented across multiple predictive depths, enabling short- and long-horizon reasoning.

### Trajectory Selection (E3)  
Future action is chosen by evaluating candidate trajectories against reality, ethics, and residue under precision control.

### Ethical Cost M  
Ethical cost is the predicted degradation of:
- the self-model, and
- mirrored other-models,  
discounted by coupling strength.

### Moral Residue R  
Residue is persistent geometric deformation of latent space caused by harm, shaping future choice.

### Precision Control  
Precision modulates commitment, exploration, and error weighting across depths.

### Offline Integration (Sleep)  
Offline processes consolidate reality models, integrate residue, and recalibrate precision.

## 5. Social Extension (Self, Other, Language)

REE treats social cognition as **emergent reuse of core machinery**:

- **Mirror modelling**: the self generative model is reused to simulate others with reduced coupling and no interoceptive closure.
- **Social coupling** modulates ethical weight and residue formation.
- **Language** emerges as a symbolic compression layer that externalises internal state to reduce other-modelling cost, while remaining constrained by embodied harm signals.

## 6. Failure Modes (Taxonomy)

REE explicitly predicts the following failure modes:

- **Moral amnesia**: residue disabled or overwritten.
- **Residue overload**: accumulation without integration.
- **Precision collapse**: over-commitment or paralysis.
- **Social decoupling**: mirror modelling gain too low or too high.
- **Symbolic override**: language or ideology suppresses harm signals.

## 7. What Is Intentionally Open

REE deliberately does **not** fix:

- model classes,
- planners,
- embodiment level,
- training regimes,
- environments.

REE constrains **what must exist**, not **how it must be built**.

## Closing Statement

REE specifies what it means for an agent to **remain responsible for its actions across time**, even as capability increases.

If an implementation can:
- act,
- learn,
- harm,
- remember,
- and still choose differently later because of that harm,

then it is behaving as an REE-compliant system.

Everything else in this repository elaborates this core.