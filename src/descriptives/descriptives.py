from collections.abc import Sequence
from numbers import Number



def get_frequencies(data: Sequence) -> dict[str, Number]:
    cats_to_counts = {}
    for item in data:
        if item not in cats_to_counts:
            cats_to_counts[item] = 1
        else:
            cats_to_counts[item] +=1
