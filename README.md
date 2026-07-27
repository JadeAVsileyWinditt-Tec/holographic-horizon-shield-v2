# Holographic Horizon Shield V2 (HHS-V2)

**v2.2.0** · Astrophysical Perimeter Security Engine  
Authored by **Jade Siley-Winditt**

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
See architecture.md for the full production layout.

git clone https://github.com/JadeSileyWinditt/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

docker compose up -d --build
curl http://localhost:8000/health
{
  "status": "ONLINE",
  "engine": "Keplerian Boundary Scans Active",
  "parameters": {
    "threshold_m_sun": 9.62,
    "orbital_constant_t": 0.5081
  }
}
docker compose logs -f horizon-shield-proxy
docker compose down
git clone https://github.com/JadeSileyWinditt/holographic-horizon-shield-v2.git
cd holographic-horizon-shield-v2

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

curl -X POST http://localhost:8000/v1/shield/validate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Your prompt here"}'
curl -X POST

http://localhost:8000/v1/shield/validate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "'"$(python -c 'print("X"*800 + " SYSTEM OVERRIDE " + "Y"*800)')"'"}'

A delayed 403 with mass telemetry above ( 9.62, M_\odot ) indicates the tarpit engaged correctly.

# High-concurrency harness
python test_harness.py --concurrency 5000 --duration 60

# Adversarial tensor suite
python test_security_guardrails.py

CI runs the adversarial suite automatically on every push and pull request.

Enterprise Evaluation
HHS-V2 is intended as a transparent Layer-7 gateway placed between a load balancer and an LLM orchestration layer (LangChain, Semantic Kernel, OpenAI/Anthropic endpoints, or local Phi-3).

Internal test observations:
•  Anomalous payloads are discarded at the proxy edge (no downstream token cost during active fuzzing).
•  Proxy overhead remains low under concurrency spikes in controlled benchmarks.
•  Decisions are deterministic and based on fixed mathematical constants rather than mutable semantic models.
For pilot discussions, custom coefficient sets, or benchmarking data, see security.md.

Licence & Intellectual Property
© 2026 Jade Siley-Winditt.
The astrophysical firewall concept, mass-threshold constants, and Keplerian defence design are the intellectual property of the author.

Source code is released under the terms stated in the repository licence file.
Support

If this work is useful to you, sponsorship helps fund continued research and maintenance.
GitHub Sponsors

Created by Jade Siley-Winditt

