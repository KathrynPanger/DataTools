from pandas import DataFrame
from numpy import ndarray
import statsmodels.api as sm
def _parse_dv_ivs_for_statsmodel(dv_name:str, iv_names: list[str]) -> str:
    return f"{dv_name} ~ {' + '.join(iv_names)}"

def _extract_ci(results, target_iv:str, sig: float):
    table = results.conf_int(alpha = sig)
    row = table.loc[target_iv]
    return tuple(row.values)

def _extract_parameter(results, dv_name:str):
    pass

def _ivs_with_constant(df: DataFrame) -> DataFrame:
    return sm.add_constant(df)