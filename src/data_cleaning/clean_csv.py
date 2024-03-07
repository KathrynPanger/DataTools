import pandas as pd
from pandas._libs.internals import defaultdict
from unidecode import unidecode
#TODO: test these and cleaning functions

def convert_utf8(original_file_path: str, new_file_path: str):
    df = pd.read_csv(original_file_path, converters=defaultdict(lambda i: str))
    for column in df.columns:
        df[column] = df[column].apply(lambda x: unidecode(str(x)))
    df.to_csv(new_file_path, encoding='utf-8')