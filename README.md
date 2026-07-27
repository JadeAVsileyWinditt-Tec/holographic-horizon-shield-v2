# Holographic Horizon Shield V2 (HHS-V2)

**v2.2.0** · Astrophysical Perimeter Security Engine  
Authored by **Jade Siley-Winditt**

[![CI](https://github.com/JadeSileyWinditt/holographic-horizon-shield-v2/actions/workflows/ci.yml/badge.svg)](https://github.com/JadeSileyWinditt/holographic-horizon-shield-v2/actions)
[![License](https://img.shields.io/badge/License-Source%20Available-blue.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Jade%20Siley%20Winditt-informational)](https://github.com/JadeSileyWinditt)

A stateless, high-concurrency Layer-7 API proxy for real-time detection and containment of adversarial LLM prompts.  
HHS-V2 evaluates inbound text as a physical payload crossing a gravitational boundary, using calculations derived from the **Gaia BH1** binary system — the nearest known black hole to Earth.

> **Status:** Alpha prototype. Core Keplerian engine and asynchronous tarpit are operational.  
> High-concurrency behaviour (>5,000 RPS) and multi-language coefficient calibration remain under active evaluation.  
> **Not recommended for mission-critical production use without isolated sandbox testing.**

This is a solo research project. Bug reports are welcome; larger contributions are batched against a fixed research timeline.

**Licence:** Source-available. See [`LICENSE`](./LICENSE) for full terms.  
© 2026 Jade Siley-Winditt. The astrophysical firewall concept, mass-threshold constants, and Keplerian defence design remain the intellectual property of the author.

---

## Features

- Deterministic Keplerian boundary scan (no ML classifiers)
- Asynchronous tarpit containment that drains attacker resources
- FastAPI production gateway with health telemetry
- Structured adversarial tensor test suite
- Automated CI security scanning on every push and pull request
- Docker Compose deployment for local evaluation
- Designed to sit in front of LangChain, Semantic Kernel, Phi-3, or any LLM endpoint

---

## Theoretical Foundation

HHS-V2 replaces conventional classification models with a physical defensive metaphor.  
Exact constants from the Gaia BH1 system are mapped into software gatekeepers.

### Core Calculations

Structural density of incoming text is scored with a Newtonian form of Kepler’s Third Law:

\[
\text{Variance} = \sum \left( \frac{\text{Count of Character}}{\text{Total Length}} \right)^2
\]

\[
a = 1.0 + (\text{Variance} \times 5.0)
\]

\[
M = \frac{a^3}{T^2}
\]

### Boundary Constants

| Constant                  | Value                                      | Role                                      |
|---------------------------|--------------------------------------------|-------------------------------------------|
| Orbital period \( T \)    | \( 185.59 / 365.25 \approx 0.5081 \) yr   | Temporal baseline                         |
| Event-horizon threshold   | \( 9.62\, M_\odot \)                       | Mass limit that triggers containment      |
| Distance constraint       | 1,560.4 ly                                 | Token chaotic-drift monitor               |

When calculated mass \( M \) exceeds \( 9.62\, M_\odot \), the request is treated as a **Horizon Breach** and diverted into the tarpit.

---

## Tarpit Defence

On a horizon breach the engine:

1. Flags the request as anomalous  
2. Engages a non-blocking asynchronous stall (`asyncio.sleep`)  
3. Holds the connection open, forcing automated tools to consume compute while waiting for a response

---

## Architecture

```text
[Inbound Prompt]
        │
        ▼
┌──────────────────────────┐
│  FastAPI Gateway         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  GeometricEngine         │
│  (Keplerian mass scan)   │
└────────────┬─────────────┘
             │
      ┌──────┴──────┐
      │             │
  [Clean]       [Breach]
      │             │
      ▼             ▼
 Forward to     Async Tarpit
 LLM            (resource drain)
