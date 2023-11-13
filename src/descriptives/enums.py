import enum

class ParameterType(enum.Enum):
    BETA = "β"
    INTERCEPT = "α"

class TestStatisticType(enum.Enum):
    T="t"
    F="F"