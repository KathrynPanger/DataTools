from regression.linear_regression import RegressionModel
import pytest
import pandas as pd
import yaml

# An amount by which results can be "off" from expected values
# due to rounding
ROUNDING_ERROR = 0.0005


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


def test_regression_results_betas(regression_data, expected_regression_results):
    dv_name = "A"
    iv_names = ["B","C"]
    sig_level = 0.05

    model = RegressionModel(df=regression_data,
                            dv_name=dv_name,
                            iv_names=iv_names,
                            sig_level=sig_level)

    # Get parameter and associated t properties
    expected_properties = expected_regression_results["parameter_properties"]

    model_betas = model.betas
    for iv_name in iv_names:
        beta = model_betas[iv_name]
        expected_value = expected_properties["beta_value"][iv_name]
        expected_t = expected_properties["t_test"][iv_name]
        expected_p = expected_properties["p_value"][iv_name]
        expected_se = expected_properties["se"][iv_name]
        ## YAMIL files cannot handle tuples, we must cast it
        expected_ci = tuple(expected_properties["conf_interval"][iv_name])
        # beta
        assert beta.value == pytest.approx(expected_value, abs=ROUNDING_ERROR)

        # t-value
        assert beta.t.value == pytest.approx(expected_t, abs=ROUNDING_ERROR)

        # p-value
        assert beta.t.p == pytest.approx(expected_p, abs=ROUNDING_ERROR)

        # standard error
        assert beta.t.se == pytest.approx(expected_se, abs=ROUNDING_ERROR)

        # confidence interval
        assert beta.t.ci == pytest.approx(expected_ci, abs=ROUNDING_ERROR)

def test_regression_results_pre_model_properties(regression_data, expected_regression_results):

   dv_name = "A"
   iv_names = ["B","C"]
   sig_level = 0.05
   model = RegressionModel(df=regression_data,
                            dv_name=dv_name,
                            iv_names=iv_names,
                            sig_level=sig_level)
   # pre-regression properties
   expected_pre_reg_properties = expected_regression_results["pre_regression_properties"]
   expected_N = expected_pre_reg_properties["N"]
   expected_iv_count =  expected_pre_reg_properties["iv_count"]
   expected_beta_degrees_freedom = expected_pre_reg_properties["beta_degrees_freedom"]
   assert model.N == expected_N
   assert model.iv_count == expected_iv_count
   assert model.beta_degrees_freedom == expected_beta_degrees_freedom

def test_regression_results_post_model_properties(regression_data, expected_regression_results):

   dv_name = "A"
   iv_names = ["B","C"]
   sig_level = 0.05
   model = RegressionModel(df=regression_data,
                            dv_name=dv_name,
                            iv_names=iv_names,
                            sig_level=sig_level)

   # post-regression properties
   expected_model_properties = expected_regression_results["model_properties"]
   # R2
   expected_r2 = expected_model_properties["r2"]
   expected_r2_adj = expected_model_properties["r2_adj"]\

   assert model.r2 == pytest.approx(expected_r2, abs=ROUNDING_ERROR)
