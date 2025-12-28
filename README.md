# CubeSat 1U — COMMS-first (UHF baseline)
[![CI](https://github.com/SvetLuna-Lab/cubesat-1u-comms-first/actions/workflows/ci.yml/badge.svg)](https://github.com/SvetLuna/cubesat-1u-comms-first/actions/workflows/ci.yml)

COMMS-first engineering skeleton for a 1U CubeSat: a reproducible pipeline from mission assumptions to an actionable radio link.

**Core idea:** if the radio link is not closed, nothing else matters. This repo treats communications as the primary system driver.

## Why this matters
CubeSat teams often treat communications as an “integration detail” and discover too late that the link is power-limited, antenna-limited, or operations-limited.  
This project flips the workflow: **close the link first**, then let COMMS constraints shape power, scheduling, and system priorities.

## Engineering signals (what this repo demonstrates)
- **Reproducibility:** configs are versioned (`configs/*.yaml`) and drive calculations.
- **Traceability:** assumptions → equations → outputs (no “magic numbers” hidden in notebooks).
- **Determinism:** automated tests validate framing/CRC and sanity-check budget outputs.
- **CI discipline:** lint + tests run on every push/PR (portfolio-grade hygiene).
- **Extensibility by design:** S-band path is prepared as a config+module extension, not a rewrite.

## What’s inside (v0.1.0)
- **YAML-driven link budget** calculator: FSPL, Prx, C/N0, Eb/N0.
- **LEO Doppler estimate** (order-of-magnitude for frequency planning).
- **Minimal beacon framing**: sync + length + payload + CRC16-CCITT.
- **Reproducible tests + CI**: pytest + ruff + GitHub Actions.

Baseline profile: **UHF downlink** (conservative, fast to validate).  
Extension path: **S-band profile stub** included to grow throughput later without rewriting the core.

## Repository structure
- `configs/` — baseline radio/mission profiles (UHF now, S-band stub).
- `docs/` — requirements, CONOPS, link budget notes, ground station skeleton.
- `src/` — link budget calculator + framing modules.
- `tests/` — deterministic checks for budget outputs and CRC framing.
- `.github/workflows/` — CI pipeline.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]

python -m cubesat_comms.link_budget.budget --config configs/baseline_uhf.yaml
pytest -q
ruff check src tests
```

## Outputs you should expect

The link budget script prints:

- EIRP, FSPL, Prx

- C/N0 (dBHz) and Eb/N0 (dB) at configured bitrate

- |Doppler| in Hz (LEO order)

## Design philosophy

- Traceable assumptions (configs are versioned, not “hidden in code”).

- Conservative margins over optimistic demos.

- Composable architecture: new waveforms / FEC / bands are config + modules, not rewrites.

## Roadmap

- Add sweep reports (range/bitrate sensitivity, margin maps).

- Add FEC + interleaving and BER/FER curves.

- Add ground station reference pipeline (SDR → Doppler correction → demod → deframe → decode).

- Add S-band downlink profile once the baseline is closed with margins.

## version: 0.1.0 release

## Regulatory note

Frequencies here are placeholders. Real missions must follow national regulations and coordination processes.

