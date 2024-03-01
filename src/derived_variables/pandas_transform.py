import pandas as pd


# TODO write test functions for all these
def center(df_col: pd.DataFrame):
    return df_col - df_col.mean()

# def z_normalize():
#     pass
#
# def min_max_normalize():
#     pass
#
#
def categorical_to_numeric(df_column):
    unique_dict = {df_column.unique()[i]: i for i in range(len(df_column.unique()))}
    return df_column.map(unique_dict)


#
# def to_dummy():
#     pass

#
#
# def label_quantiles(df: DataFrame, by_col_name: str, divisions: int, quantile_col_name: str):
#     n = len(df)
#     sorted_df = df.sort_values(by=by_col_name, ascending=True)
#     bucket_size = math.floor(n / divisions)
#     remainder = n % divisions
#     quantile_array = []
#     for i in range(divisions):
#         quantile = i + 1
#         quantile_array = quantile_array + [quantile] * bucket_size
#     quantile_array = quantile_array + [divisions] * remainder
#     sorted_df[quantile_col_name] = quantile_array
#     return sorted_df
#
# def chi_sq_equal_representation(categories: Sequence, observed_frequencies: Sequence) -> list[ChiSquare]:
#     n = sum(observed_frequencies)
#     category_count = len(categories)
#     degrees_of_freedom = category_count - 1
#     expected_frequency = n/category_count
#     chi_contributions = [(((observed_frequency - expected_frequency) ** 2) / expected_frequency) for observed_frequency in observed_frequencies]
#     chi_overall = sum(chi_contributions)
#     p = chi2.cdf(chi_overall, df = degrees_of_freedom)
#     chi_squares = [ChiSquare(chi_contribution=chi_contributions[i],
#                              value=chi_overall,
#                              p=p,
#                              expected_frequency=expected_frequency,
#                              observed_frequency=observed_frequencies[i],
#                              expected_relative_frequency=1/category_count,
#                              observed_relative_frequency = observed_frequencies[i]/n,
#                              ) for i in range(len(observed_frequencies))]
#     return chi_squares