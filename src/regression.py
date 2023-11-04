from pandas import DataFrame
from sklearn.linear_model import LinearRegression


class Regression:
    def __init__(self,
                 dataframe: DataFrame,
                 dependent_variable:str,
                 independent_variables:list[str],
                 ):
