from pandas import DataFrame
from pandas_helper import is_column
def z_normalize():
    pass

def min_max_normalize():
    pass

def center():
    pass
s
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