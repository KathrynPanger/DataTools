from scipy.stats import t
from abc import ABC, abstractmethod

class TestStatistic(ABC):
    def __init__(self,
                 value: float,
                 p: float,
                 se: float,
                 degrees_freedom: int
                 ):
        self.value = value
        self.p = p
        self.se = se
        self.degrees_freedom = degrees_freedom

    # Get confidence interval for the test statistic
    @abstractmethod
    def ci(self, sig_level:float) -> tuple[float, float]:
        pass

    # Get significance pass/fail for test statistic
    @abstractmethod
    def is_significant(self, sig_level:float) -> bool:
        pass


class T(TestStatistic):

    # Get confidence interval for the test statistic
    def ci(self, sig_level: float) -> tuple[float, float]:
        critical_probability = 1-sig_level
        critical_t = t.ppf(q=critical_probability,
                           df=self.degrees_freedom)
        distance_from_estimate = critical_t * self.se
        return (self.value + distance_from_estimate, self.value - distance_from_estimate,)

    # Get significance pass/fail for test statistic
    def is_significant(self, sig_level: float) -> bool:
        confidence_interval = self.ci(sig_level)
        # Confidence interval captures zero or not
        return confidence_interval[0] * confidence_interval[1] > 0
