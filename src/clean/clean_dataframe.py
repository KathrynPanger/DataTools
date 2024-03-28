from collections.abc import Callable
import pandas as pd

def clean_headers(df: pd.DataFrame, cleaning_functions_list:list[Callable]) -> pd.DataFrame:
    column_name_map = {item: item for item in df.columns}
    for item in column_name_map:
        for function in cleaning_functions_list:
            column_name_map[item] = function(column_name_map[item])
    df.rename(columns=column_name_map, inplace=True)
    return df

def clean_headers(df: pd.DataFrame,
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    column_name_map = {item: item for item in df.columns}
    for item in column_name_map:
        for function in cleaning_functions_list:
            column_name_map[item] = function(column_name_map[item])
    df.rename(columns=column_name_map, inplace=True)
    return df


# Apply a list of functions to selected columns
def clean_columns(df: pd.DataFrame,
                  selected_columns: list[str],
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    for col in selected_columns:
        for function in cleaning_functions_list:
            df[col] = df[col].apply(lambda x: function(x))
    return df


# Apply a list of functions to every single entry in the dataframe
def clean_entries(df: pd.DataFrame,
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    for function in cleaning_functions_list:
        df = df.apply(lambda x: function(x))
        return df

def cast_data_types(df: pd.DataFrame, names_to_types: dict) -> pd.DataFrame:
    return df.astype(names_to_types)

