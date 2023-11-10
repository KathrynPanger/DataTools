from pandas import DataFrame


def is_column(df: DataFrame):
    return df.shape[0] == 1