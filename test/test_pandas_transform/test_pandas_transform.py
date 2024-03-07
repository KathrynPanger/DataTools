import pandas as pd
from pandas.testing import assert_frame_equal
from derived_variables.pandas_transform import center


def test_center():
    uncentered_data = pd.DataFrame({"data":[1,2,3,4,5,6,7,8,9]})
    result = center(uncentered_data)
    expected_result = pd.DataFrame({"data": [-4,-3,-2,-1,0,1,2,3,4]})
    assert_frame_equal(result, expected_result, check_dtype=False)

def test_mean_normalize():
    pass

def test_min_max_scale_normalize():
    pass