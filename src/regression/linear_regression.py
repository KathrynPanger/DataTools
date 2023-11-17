from pandas import DataFrame
import statsmodels.api as sm
from statistical_objects.test_statistic import F
from interfaces.statsmodel_interface import _ivs_with_constant, _extract_parameters
from statsmodels.stats.stattools import robust_kurtosis
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


        ## Parameters
        self.betas = _extract_parameters(results=self.results,
                                         iv_names=self.iv_names,
                                         sig_level=self.sig_level,
                                         degrees_freedom=self.beta_degrees_freedom,
                                         )

        # TODO: Test residuals
        self.residuals = self.results.resid
        self.residuals_normalized = self.results.resid_pearson

        ## Shape
        # self.kurtosis = robust_kurtosis(y=self.results.resid_pearson)
        self.skew = skew(self.residuals_normalized)


        # Create Printable Summary
        self.summary = self.results.summary(alpha=self.sig_level)
