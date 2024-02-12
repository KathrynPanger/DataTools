from typing import NamedTuple

from scipy.stats import t
from abc import ABC, abstractmethod
from statistical_objects.enums import TestStatisticType

class ConfidenceInterval(NamedTuple):
    lower: float
    upper: float

class TestStatistic():
    def __init__(self,
                 type_: TestStatisticType,
                 value: float,
                 p: float):
        self.type_ = type_
        self.value = value
        self.p = p

    def __repr__(self):
        return (f"TestStatistic(type_='{self.type_}', "
                f"value={round(self.value, 3)}, "
                f"p={round(self.p, 3)}")


class T(TestStatistic):
    def __init__(self,
                 value: float,
                 p: float,
                 se: float,
                 degrees_freedom: int,
                 sig_level: float,
                 ci: ConfidenceInterval,
                 ):
        super().__init__(type_=TestStatisticType.T,
                         value=value,
                         p=p)
        self.se = se
        self.degrees_freedom = degrees_freedom
        self.sig_level = sig_level
        self.ci = ci
        # Determine whether confidence interval captures zero (think about it).
        self.reject_H0 = self.ci.upper * self.ci.lower > 0
    def __repr__(self):
        return (f"T(type_='{self.type_}', "
                f"value={round(self.value,3)}, "
                f"p={round(self.p,3)}, "
                f"se={round(self.se)}, "
                f"degrees_freedom={self.degrees_freedom},"
                f"sig_level={self.sig_level},"
                f"ci={self.ci},"
                f"reject_H0={self.reject_H0}")
class F(TestStatistic):
    def __init__(self, value, p):
        super().__init__(type_=TestStatisticType.F,
                     value=value,
                     p=p)

class JBerra(TestStatistic):
    def __init__(self, value, p):
        super().__init__(type_=TestStatisticType.J_BERRA,
                     value=value,
                     p=p)

class ChiSquare(TestStatistic):
    def __init__(self, value, p, expected, observed):
        super().__init__(type_=TestStatisticType.CHI_SQUARE,
                     value=value,
                     p=p)
        self.expected = expected
        self.observed = observed
