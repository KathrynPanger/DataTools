from collections.abc import Sequence, Collection
from numbers import Number
import pandas as pd

def get_frequencies(df: pd.DataFrame, col_name: str) -> dict[str, list[Number]]:
    unique_values = set(df[col_name])
    cats_to_counts = {"value": [], "count": []}
    for cat in unique_values:
        cats_to_counts["value"].append(cat)
        cats_to_counts["count"].append(len(df.loc[df[col_name] == cat]))
    return cats_to_counts


def describe_categorical(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
    summary = pd.DataFrame(get_frequencies(df, col_name))
    n = len(summary)
    summary["relative_frequency"] = summary["count"]/n
    return summary


def describe_continuous(df: pd.DataFrame, col_name: str) -> dict[str, Number]:
    col = df[col_name]
    q1 = col.quantile(0.25)
    mean = col.mean()
    q3 = col.quantile(0.75)
    median = col.median()
    max = col.max()
    min = col.min()
    std = col.std()
    summary = {"variable": [col_name], "q1": [q1], "mean": [mean], "q3": [q3], "median": [median], "min": [min],
               "max": [max], "std": [std]}
    return summary



# Produces dataframe of STATA-like summary statistics
# for any number of variables from the same dataframe
def describe_many_continuous(df:pd.DataFrame, varlist: list[str]) -> pd.DataFrame:
    summary_df = pd.DataFrame()
    for i in range(len(varlist)):
        one_variable = pd.DataFrame(describe_continuous(df=df, col_name=varlist[i]))
        if i == 0:
            summary_df = one_variable
        else:
            summary_df = pd.concat([summary_df, one_variable], ignore_index=True)
    return summary_df.set_index("variable")