from regression.linear_regression import RegressionModel
import pytest
import pandas as pd
import yaml
import os
@pytest.fixture
def regression_data():
    path = "test_regression/test_data.csv"
    df = pd.read_csv(path)
    return df

@pytest.fixture
def expected_regression_results():
    expected_results_path = "test_regression/expected_results.yaml"
    with open(expected_results_path, 'r') as file:
        expected_results = yaml.safe_load(file)
    return expected_results


def test_regression_results(regression_data, expected_regression_results):
    measurement_error = 0.01
    model = RegressionModel(df=regression_data,
                            dv_name="A",
                            iv_names=["B","C"],
                            sig=0.05)
    expected_r2 = expected_regression_results["r2"]
    assert model.r2 == pytest.approx(expected_r2, measurement_error)
