from collections.abc import Sequence, Mapping
from numbers import Number


from pandas import DataFrame
import statsmodels.api as sm
from statistical_objects.test_statistic import F, JBerra
from interfaces.statsmodel_interface import _ivs_with_constant, _extract_parameters, _extract_jarque_berra_skew_kurtosis
from statsmodels.stats.stattools import robust_kurtosis, durbin_watson, jarque_bera
from scipy.stats import skew, kurtosis

#TODO heterosketasticity tests, explanation of each statistic interpretation

class RegressionModel:
    def __init__(self,
                 df: DataFrame,
                 dv_name:str,
                 iv_names:list[str],
                 sig_level: float):

        # Collect Inputs
        self.df = df
        self.dv_name = dv_name
        self.iv_names = iv_names
        self.sig_level = sig_level

        # Select Data
        self.dv = self.df[dv_name]
        self.ivs = _ivs_with_constant(self.df[[iv for iv in iv_names]])

        # Derive Pre-Model Vars
        self.N = len(df)
        self.iv_count = len(self.iv_names)
        self.beta_degrees_freedom = self.N - self.iv_count - 1

        # Fit the model
        self.model = sm.OLS(self.dv, self.ivs)
        self.results = self.model.fit()

        # Derive Post-Model Vars
        ## Model Descriptives
        self.r2 = self.results.rsquared
        self.r2_adj = self.results.rsquared_adj
        self.f = F(value=self.results.fvalue, p=self.results.f_pvalue)
        self.log_likelihood = self.results.llf


        ## Parameters
        self.parameters = _extract_parameters(results=self.results,
                                              iv_names=self.iv_names,
                                              sig_level=self.sig_level,
                                              degrees_freedom=self.beta_degrees_freedom,
                                              )

        # TODO: Test residuals
        self.residuals = self.results.resid
        self.residuals_normalized = self.results.resid_pearson

        # Model Tests
        self.d_watson = durbin_watson(self.results.resid)
        self.jarque_berra, self.skew, self.kurtosis = _extract_jarque_berra_skew_kurtosis(self.residuals_normalized)

        self.aic = self.results.aic
        self.bic = self.results.bic
        self.cond_no = self.results.condition_number

# TODO make and test command to predict new values from parameters (below)

    def predict_y_from_values(self, proposed_dv_values: Mapping[str:Number]):
        betas = self.parameters
        # Calculate result: start with 0, add intercept
        # y = a + b_0 + b_1 ... + b_n
        result = betas.pop("const").value
        # Make sure user-entered variable names are correct
        assert proposed_dv_values.keys() == betas.keys(), "Variable names and quantity must match fitted model."
        for variable_name in proposed_dv_values.keys():
            # Adding slope * value to th
            result += (betas[variable_name].value * proposed_dv_values[variable_name])
        return result

# TODO make and test summarize command (below)
        ## Create printable summary
        # def summarize():
        # return self.results.summary(alpha=self.sig_level)


