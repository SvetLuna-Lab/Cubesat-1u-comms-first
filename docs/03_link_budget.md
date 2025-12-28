# 03 — Link Budget

This document is intentionally mirrored by code (`src/.../budget.py`).
The source of truth is the calculator output for a given `configs/*.yaml`.

## Assumptions (baseline)
- Slant range: 1200 km (conservative mid-pass)
- Relative speed: 7.5 km/s (LEO order)
- Ground Rx gain: 12 dBi (small directional antenna)
- System noise temperature: 450 K (order-of-magnitude)

## Outputs we track (v0.1.0)
- EIRP (dBm)
- FSPL (dB)
- Prx (dBm)
- C/N0 (dBHz)
- Eb/N0 at configured bitrate (dB)
- |Doppler| (Hz)

## What “good” looks like
Not “maximum optimism”, but stable positive margins under conservative ranges.
