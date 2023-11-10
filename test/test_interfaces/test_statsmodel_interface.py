
from interfaces.statsmodel_interface import _parse_dv_ivs_for_statsmodel


def test_parse_dv_ivs_for_statsmodel():
    dv = "weight"
    ivs = ["diet", "hours_exercised", "age"]
    result = _parse_dv_ivs_for_statsmodel(dv, ivs)
    expected_result = 'weight ~ diet + hours_exercised + age'
    assert result == expected_result