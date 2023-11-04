from pandas import DataFrame
from sklearn.linear_model import LinearRegression


class RegressionModel:
    def __init__(self,
                 dataframe: DataFrame,
                 dependent_variable:str,
                 independent_variables:list[str],
                 ):
        self.df = dataframe
        self.dv = self.df[dependent_variable]
        self.ivs = self.df[[iv for iv in independent_variables]]
