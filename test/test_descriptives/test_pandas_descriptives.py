import pytest
import pandas as pd

from descriptives.pandas_descriptives import summarize_one, describe_one


@pytest.fixture
def pandas_data():
    path = "test_descriptives/pandas_descriptives_test_data.csv"
    df = pd.read_csv(path)
    return df
def test_summarize_one(pandas_data):
    result = summarize_one(df=pandas_data, col_name="int_var")
    assert result == {"variable": "int_var",
                      "q1": [1],
                      "mean": [1.25],
                      "q3": [1.25],
                      "median": [1],
                      "min": [1],
                      "max": [2],
                      "std": [0.5]
                      }
def test_describe_one(pandas_data):
    description = describe_one(df=pandas_data, col_name="cat_var")
    print(description)