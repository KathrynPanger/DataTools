from regression.regression_helper import parse_ivs_for_patsy

def test_parse_ivs_for_patsy():
    test_input = ["first_name", "last_name", "email"]
    output = parse_ivs_for_patsy(test_input)
    expected_output = "first_name + last_name + email"
    assert output == expected_output
