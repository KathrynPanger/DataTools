from collections.abc import Callable
import pandas as pd

def clean_columns(df: pd.DataFrame, cleaning_functions_list:list[Callable]) -> pd.DataFrame:
    column_name_map = {item: item for item in df.columns}
    for item in column_name_map:
        for function in cleaning_functions_list:
            column_name_map[item] = function(column_name_map[item])
    df.rename(columns=column_name_map, inplace=True)
    return df

