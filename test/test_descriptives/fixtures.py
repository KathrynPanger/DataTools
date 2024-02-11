import pandas as pd

@pytest.fixture
def pandas_descriptives_test_data():
    path = "pandas_desriptives_test_data.csv"
    df = pd.read_csv(path)
    return df