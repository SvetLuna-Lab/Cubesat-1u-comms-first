# CubeSat 1U — COMMS-first (UHF baseline)

This repository is a COMMS-first engineering skeleton for a 1U CubeSat:
link budget → Doppler → framing/CRC → reproducible tests & CI artifacts.

## Why COMMS-first
If the radio link is not closed, nothing else matters. This project treats
communications as the primary system driver (power, pointing, scheduling).

## v0.1.0 scope
- Parametric link budget calculator (Python, YAML configs)
- Doppler shift estimation for LEO
- Minimal beacon framing (sync word + length + payload + CRC16-CCITT)
- CI with pytest (reproducible, deterministic checks)

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]

python -m cubesat_comms.link_budget.budget --config configs/baseline_uhf.yaml
```
## Safety / compliance note

Frequencies here are placeholders. Real missions must follow national
regulations and coordination processes (e.g., IARU where applicable).

## Roadmap (future)

- Add S-band downlink profile (kept as config-only extension)

- Coding/FEC (convolutional + interleaving) + BER/FER curves

- Ground station reference pipeline (SDR → demod → deframe → decode)


---


