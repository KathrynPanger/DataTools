from typing import NamedTuple
from descriptives.enums import TestStatisticType
from descriptives.test_statistic import TestStatistic

class Parameter(NamedTuple):
    type_: TestStatisticType
    value: float
    t: TestStatistic
