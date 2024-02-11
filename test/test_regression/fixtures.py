import pytest
import pandas as pd
import yaml

@pytest.fixture
def regression_data():
    path = "test_regression_data.csv"
    df = pd.read_csv(path)
    return df

@pytest.fixture
def expected_regression_results():
    expected_results_path = "expected_results.yaml"
    with open(expected_results_path, 'r') as file:
        expected_results = yaml.safe_load(file)
    return expected_results


