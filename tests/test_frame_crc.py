from cubesat_comms.framing.beacon_frame import build_baseline_beacon, crc16_ccitt


def test_frame_crc_matches():
    payload = b"\x01\x02\x03hello"
    frame = build_baseline_beacon(payload)

    sync = frame[:4]
    length = frame[4]
    body = frame[:5 + length]  # sync + len + payload
    crc_read = int.from_bytes(frame[5 + length: 7 + length], "big")

    crc_calc = crc16_ccitt(body)
    assert crc_read == crc_calc
