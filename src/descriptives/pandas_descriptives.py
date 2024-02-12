from collections.abc import Sequence
from numbers import Number
import pandas as pd
from scipy.stats import chisquare

from statistical_objects.test_statistic import ChiSquare


# TODO: test all these fuctions

# Produces STATA-like summary statistics in
# either a dataframe or dictionary, as specified by user



def summarize_one(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
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

def _unique_value_counts(df: pd.DataFrame, col_name: str) -> list[list[str, Number]]:
    unique_values = df[col_name].unique()
    cats_to_counts = []
    for cat in unique_values:
        count = len(df.loc[df[col_name] == cat])
        cats_to_counts.append([cat, count])
    return cats_to_counts


def _chi_sq_equal_representation(df: pd.DataFrame, cat_col_name: str, count_col_name: str) -> pd.DataFrame:
    counts = list(df[count_col_name])
    chi_list = chisquare(counts)
    expected = sum(counts)/len(counts)
    results = []
    for i in range(len(counts)):
        chi_square = ChiSquare(value=chi_list[i][0],
                               p=chi_list[i][1],
                               observed=counts[i],
                               expected=expected,
                               )
        results.append(chi_square)

    return results


def describe_one(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
    summary = pd.DataFrame(_unique_value_counts(df, col_name), columns = [col_name, "count"])
    n = len(summary)
    summary["percent"] = summary["count"]/n
    summary["chi_sq_equal_rep"] = _chi_sq_equal_representation(df=summary, cat_col_name=col_name, count_col_name = "count")
    return summary




# Produces dataframe of STATA-like summary statistics
# for any number of variables from the same dataframe
def summarize_many(df:pd.DataFrame, varlist: list[str]) -> pd.DataFrame:
    summary_df = pd.DataFrame()
    for i in range(len(varlist)):
        one_variable = pd.DataFrame(summarize_one(df=summary_df, col_name=varlist[i]))
        if i == 0:
            summary_df = one_variable
        else:
            summary_df = pd.concat([summary_df, one_variable], ignore_index=True)
    return summary_df.set_index("variable")