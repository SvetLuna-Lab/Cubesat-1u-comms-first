from cubesat_comms.link_budget.budget import compute_budget


def test_budget_outputs_are_finite():
    res = compute_budget("configs/baseline_uhf.yaml")
    assert abs(res.eirp_dbm) < 200
    assert 0 < res.path_loss_db < 300
    assert -200 < res.prx_dbm < 50
    assert -50 < res.ebn0_db < 100
    assert res.doppler_hz_abs > 0
