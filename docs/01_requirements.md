# 01 — Requirements (COMMS-first)

## Primary goal
Close the downlink with deterministic decoding and measurable margins.

## Baseline (v0.1.0)
- Band: UHF downlink (placeholder frequency)
- Bitrate: 9600 bps (baseline)
- Frame: sync + length + payload + CRC16
- Doppler: accounted for in frequency planning (estimate produced)
- Deliverable: reproducible link budget + framing tests + CI green

## Constraints (engineering)
- Power budget must tolerate duty cycle planning (beacon always wins)
- Antenna strategy must be deployable or body-mounted with known pattern
- Regulatory/coordination is mandatory before real frequency selection
