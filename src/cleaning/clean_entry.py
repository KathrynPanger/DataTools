import re
from numbers import Number
import pandas as pd

# TODO test functions for all of these

# Remove special characters when dealing with words
# transforms removed characters into spaces, removes . and -
def remove_special_for_words(entry: str | Number):
    return re.sub(r"[^a-zA-Z0-9]+", ' ', str(entry))

# Remove special characters when dealing with numbers
# No spaces, does not remove - and .
def remove_special_for_numbers(entry: str | Number):
    return re.sub(r"[^a-zA-Z0-9-.]+", '', str(entry))

# Remove leading and trailing spaces
def truncate(entry: str | Number):
    return str(entry).strip()

# Replace spaces with underscores
def snake_case(entry: str | Number):
    return str(entry).replace(" ", "_")

# Make all letters lowercase
def lower_case(entry: str | Number):
    return str(entry).lower()

def remove_spaces(entry: str | Number):
    return str(entry).replace(" ", "")

def cast_to_datetime(entry: str | Number):
    return pd.to_datetime(str(entry))