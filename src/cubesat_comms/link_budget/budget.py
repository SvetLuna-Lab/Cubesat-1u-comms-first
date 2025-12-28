from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

from cubesat_comms.config import load_config


K_DBW_PER_K_PER_HZ = -228.6  # Boltzmann constant in dBW/K/Hz


def dbm_to_dbw(dbm: float) -> float:
    return dbm - 30.0


def fspl_db(distance_m: float, freq_hz: float) -> float:
    # Free-space path loss: 20log10(4πd/λ)
    c = 299_792_458.0
    wavelength = c / freq_hz
    return 20.0 * math.log10(4.0 * math.pi * distance_m / wavelength)


def doppler_hz(v_rel_mps: float, freq_hz: float) -> float:
    c = 299_792_458.0
    return (v_rel_mps / c) * freq_hz


@dataclass(frozen=True)
class BudgetResult:
    eirp_dbm: float
    path_loss_db: float
    prx_dbm: float
    cn0_dbhz: float
    ebn0_db: float
    doppler_hz_abs: float


def compute_budget(config_path: str) -> BudgetResult:
    cfg = load_config(config_path)

    d_m = cfg.mission.slant_range_km * 1000.0
    f_hz = cfg.radio.downlink_freq_hz

    eirp_dbm = (
        cfg.radio.tx_power_dbm
        - cfg.radio.tx_line_loss_db
        + cfg.radio.tx_antenna_gain_dbi
    )

    l_fspl = fspl_db(distance_m=d_m, freq_hz=f_hz)

    # Received power
    prx_dbm = (
        eirp_dbm
        - l_fspl
        - cfg.radio.misc_losses_db
        + cfg.radio.rx_antenna_gain_dbi
        - cfg.radio.rx_line_loss_db
    )

    # C/N0 in dBHz:
    # C/N0 = Prx(dBW) - (k(dBW/K/Hz) + 10log10(Tsys))
    prx_dbw = dbm_to_dbw(prx_dbm)
    cn0_dbhz = prx_dbw - (K_DBW_PER_K_PER_HZ + 10.0 * math.log10(cfg.radio.system_noise_temp_k))

    # Eb/N0 = C/N0 - 10log10(Rb)
    ebn0_db = cn0_dbhz - 10.0 * math.log10(cfg.radio.bitrate_bps)

    doppler_abs = abs(doppler_hz(cfg.mission.v_rel_mps, f_hz))

    return BudgetResult(
        eirp_dbm=eirp_dbm,
        path_loss_db=l_fspl,
        prx_dbm=prx_dbm,
        cn0_dbhz=cn0_dbhz,
        ebn0_db=ebn0_db,
        doppler_hz_abs=doppler_abs,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="Path to YAML config")
    args = ap.parse_args()

    res = compute_budget(args.config)

    print("=== Link Budget (COMMS-first) ===")
    print(f"EIRP:         {res.eirp_dbm:8.2f} dBm")
    print(f"FSPL:         {res.path_loss_db:8.2f} dB")
    print(f"Prx:          {res.prx_dbm:8.2f} dBm")
    print(f"C/N0:         {res.cn0_dbhz:8.2f} dBHz")
    print(f"Eb/N0:        {res.ebn0_db:8.2f} dB  (at configured bitrate)")
    print(f"|Doppler|:    {res.doppler_hz_abs:8.2f} Hz (LEO order)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
