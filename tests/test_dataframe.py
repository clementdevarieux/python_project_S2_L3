import pytest
from src.MyBear.dataframe import DataFrame


@pytest.fixture
def dataframe():
    return DataFrame(["column1", "column2"], [1, 2, 3], [4, 5, 6])


def test_dataframe_is_dataframe_class(dataframe):
    assert isinstance(dataframe, DataFrame) == True


def test_dataframe_values(dataframe):
    assert dataframe.values == [[1, 2, 3], [4, 5, 6]]
