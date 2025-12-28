from __future__ import annotations

from dataclasses import dataclass


def crc16_ccitt(data: bytes, poly: int = 0x1021, init: int = 0xFFFF) -> int:
    crc = init
    for b in data:
        crc ^= (b << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) & 0xFFFF) ^ poly
            else:
                crc = (crc << 1) & 0xFFFF
    return crc & 0xFFFF


@dataclass(frozen=True)
class BeaconFrame:
    sync: bytes        # fixed pattern
    payload: bytes     # telemetry bytes

    def pack(self) -> bytes:
        # Format: SYNC (4) | LEN (1) | PAYLOAD (N) | CRC16 (2)
        if len(self.sync) != 4:
            raise ValueError("sync must be 4 bytes")
        if len(self.payload) > 255:
            raise ValueError("payload too long")

        body = bytes([len(self.payload)]) + self.payload
        crc = crc16_ccitt(self.sync + body).to_bytes(2, "big")
        return self.sync + body + crc


def build_baseline_beacon(payload: bytes) -> bytes:
    sync = bytes.fromhex("1ACFFC1D")  # common sync word (example)
    return BeaconFrame(sync=sync, payload=payload).pack()
