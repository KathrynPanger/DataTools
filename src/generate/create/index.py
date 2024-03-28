import uuid
import random
from numbers import Number
from typing import Optional
import pandas as pd


# Get a deterministic hash of a string, dependent only on the seed
# (for creating unique id columns which will always be consistent when fed the same data and seed, even if generated at different times)
def deterministic_uuid(entry: str | Number):
    random.seed(str(entry))
    unique_id = uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)
    unique_id = str(unique_id).replace("-", "")
    return unique_id

# Create a unique index column by taking a deterministic hash of values in selected identifier columns
def set_unique_index(df: pd.DataFrame, columns_to_hash: list[str], index_name="id",
                     index_length_limit: Optional[int] = None):
    df[index_name] = list(
        map(lambda x: deterministic_uuid(''.join([str(col_value) for col_value in x]))[0:index_length_limit],
            df[columns_to_hash].values))
    df.set_index(index_name, inplace=True)
    return df