from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass(frozen=True)
class MissionCfg:
    name: str
    orbit_altitude_km: float
    slant_range_km: float
    v_rel_mps: float


@dataclass(frozen=True)
class RadioCfg:
    downlink_freq_hz: float
    tx_power_dbm: float
    tx_line_loss_db: float
    tx_antenna_gain_dbi: float
    rx_antenna_gain_dbi: float
    rx_line_loss_db: float
    misc_losses_db: float
    system_noise_temp_k: float
    bitrate_bps: float


@dataclass(frozen=True)
class Config:
    mission: MissionCfg
    radio: RadioCfg


def load_config(path: str | Path) -> Config:
    p = Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))

    m = data["mission"]
    r = data["radio"]

    mission = MissionCfg(
        name=str(m["name"]),
        orbit_altitude_km=float(m["orbit_altitude_km"]),
        slant_range_km=float(m["slant_range_km"]),
        v_rel_mps=float(m["v_rel_mps"]),
    )

    radio = RadioCfg(
        downlink_freq_hz=float(r["downlink_freq_hz"]),
        tx_power_dbm=float(r["tx_power_dbm"]),
        tx_line_loss_db=float(r["tx_line_loss_db"]),
        tx_antenna_gain_dbi=float(r["tx_antenna_gain_dbi"]),
        rx_antenna_gain_dbi=float(r["rx_antenna_gain_dbi"]),
        rx_line_loss_db=float(r["rx_line_loss_db"]),
        misc_losses_db=float(r["misc_losses_db"]),
        system_noise_temp_k=float(r["system_noise_temp_k"]),
        bitrate_bps=float(r["bitrate_bps"]),
    )

    return Config(mission=mission, radio=radio)
