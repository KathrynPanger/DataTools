import pytest
import pandas as pd

from descriptives.pandas_descriptives import describe_continuous, describe_continuous, describe_categorical, \
    get_frequencies, describe_many_continuous
from pandas.testing import assert_frame_equal


@pytest.fixture
def pandas_data():
    path = "test_descriptives/pandas_descriptives_test_data.csv"
    df = pd.read_csv(path)
    return df
def test_describe_continuous(pandas_data):
    result = describe_continuous(df=pandas_data, col_name="int_var")
    assert result == {
        "variable": ["int_var"],
                      "q1": [1],
                      "mean": [2],
                      "q3": [3],
                      "median": [2],
                      "min": [1],
                      "max": [3],
                      "std": [1],
    }

def test_get_frequencies(pandas_data):
    result = get_frequencies(df=pandas_data, col_name="cat_var")
    expected_result = {'value': ['TM', 'NB', 'Female', 'Male', 'TW'], 'count': [1, 1, 2, 2, 1]}
    expected_result_df =pd.DataFrame(expected_result).sort_values(by="value").set_index(keys="value")
    result_df = pd.DataFrame(result).sort_values(by="value").set_index(keys="value")
    print(result_df)
    print(expected_result_df)
    assert_frame_equal(result_df, expected_result_df, check_dtype=False)

def test_describe_categorical(pandas_data):
    result = describe_categorical(df=pandas_data, col_name="cat_var").set_index(keys="value").sort_values(by="value")
    expected_result_dict = {'value':
                                ['TM', 'NB', 'Female', 'Male', 'TW'],
                            'count':
                                [1, 1, 2, 2, 1],
                            'relative_frequency':
                                [0.2, 0.2, 0.4, 0.4, 0.2]
                            }
    expected_result = pd.DataFrame(expected_result_dict).set_index(keys="value").sort_values(by="value")
    assert_frame_equal(result, expected_result, check_dtype=False)

def test_describe_many_continuous(pandas_data):
    result = describe_many_continuous(df=pandas_data, varlist=["int_var", "float_var"]).sort_values("variable")
    expected_result = pd.DataFrame({
        'variable':
            ['int_var', 'float_var'],
        'q1':
        [1,1.5],
        'mean':
        [2,1.642857],
        'q3':
        [3,1.5],
        "median":
        [2,1.5],
        'min':
        [1,0.5],
        'max':
        [3,3.5],
        'std':
        [1, 0.899735]
    }
    ).set_index("variable").sort_values("variable")
    assert_frame_equal(result, expected_result, check_dtype=False)