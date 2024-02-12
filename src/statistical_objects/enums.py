import enum
class ReturnTypes:
    DATAFRAME = "dataframe"
    DICTIONARY = "dictionary"

class ParameterType(enum.Enum):
    BETA = "beta"
    INTERCEPT = "intercept"


class TestStatisticType(enum.Enum):
    T="t"
    F="F"
    J_BERRA = "j_berra"
    CHI_SQUARE = "chi_square"