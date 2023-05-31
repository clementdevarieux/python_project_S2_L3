import pytest
from src.MyBear.dataframe import DataFrame


@pytest.fixture
def dataframe():
    return DataFrame(["column1", "column2"], [1, 2, 3], [4, 5, 6])


@pytest
def dataframe_is_dataframe_class(dataframe):
    assert isinstance(dataframe, DataFrame) == True


def dataframe_values(dataframe):
    assert dataframe.values == [[1, 2, 3], [4, 5, 6]]


def dataframe_max(dataframe):
    assert dataframe.series.max == 6


def dataframe_min(dataframe):
    assert dataframe.series.min == 1


def dataframe_std(dataframe):
    assert dataframe.series.std == 1  # TO DO


def dataframe_mean(dataframe):
    assert dataframe.series.mean == 3.5


def dataframe_count(dataframe):
    assert dataframe.series.count == 6  # ou 2


def dataframe_missing(dataframe):
    assert dataframe.series.missing == 0


def dataframe_type(dataframe):
    assert isinstance(dataframe.type, int) == True
