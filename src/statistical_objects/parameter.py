from numbers import Number
from typing import NamedTuple
from statistical_objects.enums import TestStatisticType
from statistical_objects.test_statistic import T
from abc import ABC
class Parameter(ABC):
    def __init__(self,
                 iv_name,
                 type_:TestStatisticType,
                 value:Number,
                 t: T):
        self.iv_name = iv_name
        self.type_ = type_
        self.value = value
        self.t = t

class Beta(Parameter):
    def __str__(self):
        return (f"Beta(iv_name='{self.iv_name}', "
                f"value={round(self.value,3)}, "
                f"t={round(self.t.value,3)}, "
                f"p={round(self.t.p,3)}, "
                f"ci={(round(self.t.ci[0],3),(round(self.t.ci[1],3,)))} "
                f"reject_H0={self.t.reject_H0})")
    def __repr__(self):
        return (f"Beta(iv_name='{self.iv_name}', "
                f"type_={self.type_}, "
                f"value={round(self.value,3)}, "
                f"t={self.t})")