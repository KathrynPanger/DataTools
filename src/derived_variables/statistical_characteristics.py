def chi_sq_equal_representation(categories: Sequence, observed_frequencies: Sequence) -> list[ChiSquare]:
    n = sum(observed_frequencies)
    category_count = len(categories)
    degrees_of_freedom = category_count - 1
    expected_frequency = n/category_count
    chi_contributions = [(((observed_frequency - expected_frequency) ** 2) / expected_frequency) for observed_frequency in observed_frequencies]
    chi_overall = sum(chi_contributions)
    p = chi2.cdf(chi_overall, df = degrees_of_freedom)
    chi_squares = [ChiSquare(chi_contribution=chi_contributions[i],
                             value=chi_overall,
                             p=p,
                             expected_frequency=expected_frequency,
                             observed_frequency=observed_frequencies[i],
                             expected_relative_frequency=1/category_count,
                             observed_relative_frequency = observed_frequencies[i]/n,
                             ) for i in range(len(observed_frequencies))]
    return chi_squares