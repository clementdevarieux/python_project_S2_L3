import pytest
from src.MyBear.dataframe import DataFrame
from src.MyBear.series import Series


@pytest.fixture
def dataframe():
    return DataFrame(["column1", "column2"], [[1, 2, 3], [4, 5, 6]])


def test_dataframe_is_dataframe_class(dataframe):
    assert isinstance(dataframe, DataFrame) == True

# def test_dataframe_values(dataframe):
#     assert dataframe.values == [[1, 2, 3], [4, 5, 6]]

def test_dataframe_i_loc_n_n(dataframe):
    assert dataframe.iloc[1, 1] == 5

def test_dataframe_i_loc_a_b_n(dataframe):
    assert isinstance(dataframe.iloc[0:1, 1], Series) == True

def test_dataframe_i_loc_n_a_b(dataframe):
    assert isinstance(dataframe.iloc[1, 0:1], DataFrame) == True

def test_dataframe_i_loc_x_y_a_b(dataframe):
    assert isinstance(dataframe.iloc[0:1, 0:1], DataFrame) == True