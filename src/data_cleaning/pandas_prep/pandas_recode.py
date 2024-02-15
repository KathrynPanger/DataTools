from pandas import DataFrame
from pandas_helper import is_column

import math

# TODO write test functions for all these
def center(df_column: DataFrame):
    # Make sure df is one column only
    assert is_column(df_column)
    # Create new column name based on old column name
    old_name = df_column.columns[0]
    new_name = f"{old_name}_centered"
    centered_column = df_column.apply(lambda x: x - df_column.mean())
    centered_column.rename(columns={old_name: new_name})
    return centered_column
def z_normalize():
    pass

def min_max_normalize():
    pass


def categorical_strings_to_values():
    pass

def to_dummy():
    pass

def exponentiate(df_column: DataFrame, order:int):
    # Make sure df is one column only
    assert is_column(df_column)
    # Create new column name based on old column name
    old_name = df_column.columns[0]
    new_name = f"{old_name}_^{order}"
    # Generate new column
    new_column = df_column[{old_name}]**order
    new_column.rename(columns={old_name: new_name})
    return new_column


def label_quantiles(df: DataFrame, by_col_name: str, divisions: int, quantile_col_name: str):
    n = len(df)
    sorted_df = df.sort_values(by=by_col_name, ascending=True)
    bucket_size = math.floor(n / divisions)
    remainder = n % divisions
    quantile_array = []
    for i in range(divisions):
        quantile = i + 1
        quantile_array = quantile_array + [quantile] * bucket_size
    quantile_array = quantile_array + [divisions] * remainder
    sorted_df[quantile_col_name] = quantile_array
    return sorted_df
