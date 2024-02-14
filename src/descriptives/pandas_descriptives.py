from collections.abc import Sequence, Collection
from numbers import Number
import pandas as pd
from scipy.stats import chisquare, chi2

from statistical_objects.test_statistic import ChiSquare


# TODO: test all these fuctions

# Produces STATA-like summary statistics in
# either a dataframe or dictionary, as specified by user


def get_frequencies_pandas(df: pd.DataFrame, col_name: str) -> list[list[str, Number]]:
    unique_values = df[col_name].unique()
    cats_to_counts = []
    for cat in unique_values:
        count = len(df.loc[df[col_name] == cat])
        cats_to_counts.append([cat, count])
    return cats_to_counts


def summarize_one(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
    summary = pd.DataFrame(get_frequencies_pandas(df, col_name), columns = [col_name, "count"])
    n = len(summary)
    summary["relative_frequency"] = summary["count"]/n
    return summary


def describe_one(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
    col = df[col_name]
    q1 = col.quantile(0.25)
    mean = col.mean()
    q3 = col.quantile(0.75)
    median = col.median()
    max = col.max()
    min = col.min()
    std = col.std()
    summary = {"variable": col_name, "q1": [q1], "mean": mean, "q3": [q3], "median": [median], "min": [min],
               "max": [max], "std": [std]}
    return summary


# Produces dataframe of STATA-like summary statistics
# for any number of variables from the same dataframe
def describe_many(df:pd.DataFrame, varlist: list[str]) -> pd.DataFrame:
    summary_df = pd.DataFrame()
    for i in range(len(varlist)):
        one_variable = pd.DataFrame(describe_one(df=summary_df, col_name=varlist[i]))
        if i == 0:
            summary_df = one_variable
        else:
            summary_df = pd.concat([summary_df, one_variable], ignore_index=True)
    return summary_df.set_index("variable")