import enum

class ParameterType(enum.Enum):
    BETA = enum.auto()
    INTERCEPT = enum.auto()

class TestStatisticType(enum.Enum):
    T=enum.auto()
    F=enum.auto()