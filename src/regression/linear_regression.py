from pandas import DataFrame
import statsmodels.api as sm
from descriptives.test_statistic import TestStatistic
from interfaces.statsmodel_interface import _ivs_with_constant


class RegressionModel:
    def __init__(self,
                 df: DataFrame,
                 dv_name:str,
                 iv_names:list[str],
                 sig: float):
        self.df = df
        self.dv_name = dv_name
        self.iv_names = iv_names
        self.sig = sig

        # Fit the model
        self.dv = self.df[dv_name]
        self.ivs = _ivs_with_constant(self.df[[iv for iv in iv_names]])
        self.model = sm.OLS(self.dv, self.ivs)
        self.results = self.model.fit()

        # Printable Summary
        self.summary = self.results.summary(alpha=self.sig)

        # Parameters, model
        self.r2 = self.results.rsquared

        #Paraemeters, variables
