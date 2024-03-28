from enum import Enum
import numpy as np
from typing import NamedTuple

class Comparitor(Enum):
  GT = ">"
  GTE = ">="
  LTE = "<="
  EQ = "=="
  LT = "<"
  NE = "!="


def is_value_comparitor_quantile(quantile,
                                 value,
                                 array,
                                 comparitor):
  comparitor_string = comparitor.value
  code_string = f"{value}{comparitor_string}{np.quantile(array, quantile)}"
  result = eval(code_string)
  return int(result)