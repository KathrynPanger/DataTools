from pandas import DataFrame
from numpy import ndarray

from descriptives.enums import ParameterType, TestStatisticType
from descriptives.parameter import Parameter, Beta
from descriptives.test_statistic import T, ConfidenceInterval
import statsmodels.api as sm


def _parse_dv_ivs_for_statsmodel(dv_name:str, iv_names: list[str]) -> str:
    return f"{dv_name} ~ {' + '.join(iv_names)}"

def _extract_ci(results, target_iv:str, sig: float):
    table = results.conf_int(alpha = sig)
    row = table.loc[target_iv]
    return tuple(row.values)

def _ivs_with_constant(df: DataFrame) -> DataFrame:
    return sm.add_constant(df)



def _extract_parameters(results, iv_names: list[str], sig_level:float, degrees_freedom):
    iv_names.append("const")
    params = results.params
    ts = results.tvalues
    bses = results.bse
    cis = results.conf_int(alpha = sig_level)
    ps = results.pvalues
    parameters = {}
    for iv_name in iv_names:
        beta_value = params.loc[iv_name]
        t_value = ts.loc[iv_name]
        p = ps.loc[iv_name]
        se = bses.loc[iv_name]
        ci = ConfidenceInterval(*(cis.loc[iv_name]).values)
        t = T(value=t_value,
              p=p,
              se=se,
              degrees_freedom = degrees_freedom,
              sig_level = sig_level,
              ci=ci)
        beta = Beta(iv_name=iv_name,
                    type_=ParameterType.BETA,
                    value=beta_value,
                    t=t)
        parameters[iv_name] = beta
    return parameters

