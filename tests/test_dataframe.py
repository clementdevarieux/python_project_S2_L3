import pytest
from src.MyBear.series import Series
from src.MyBear.dataframe import DataFrame, read_csv, read_json


@pytest.fixture
def dataframe():
    return DataFrame(["column1", "column2"], [[1, 2, 3], [4, 5, 6]])


def test_dataframe_is_dataframe_class(dataframe):
    assert isinstance(dataframe, DataFrame) == True


def test_dataframe_i_loc_n_n(dataframe):
    assert dataframe.iloc[1, 1] == 5


def test_dataframe_i_loc_a_b_n(dataframe):
    assert isinstance(dataframe.iloc[0:1, 1], Series) == True


def test_read_csv_to_df():
    df_csv = read_csv("files/test_csv.csv")
    assert isinstance(df_csv, DataFrame) == True


def test_read_json_to_df():
    df_json = read_json("files/test_json.json")
    assert isinstance(df_json, DataFrame) == True


def test_df_max(dataframe):
    df_max = dataframe._max()
    assert isinstance(df_max, DataFrame) == True


def test_df_max(dataframe):
    df = dataframe._max()
    assert isinstance(df, DataFrame) == True


def test_df_min(dataframe):
    df = dataframe._min()
    assert isinstance(df, DataFrame) == True


def test_df_mean(dataframe):
    df = dataframe._mean()
    assert isinstance(df, DataFrame) == True


def test_df_std(dataframe):
    df = dataframe._std()
    assert isinstance(df, DataFrame) == True


def test_df_count(dataframe):
    df = dataframe._count()
    assert isinstance(df, DataFrame) == True


def test_df_not_right_size():
    with pytest.raises(ValueError):
        DataFrame(
            column_names=["test_1", "test2", "test3"],
            values=[[11, 21, 3, 4], [3, -4, 1, 9]],
        )


def test_dataframe_i_loc_n_a_b(dataframe):
    assert isinstance(dataframe.iloc[1, 0:1], DataFrame) == True


def test_dataframe_i_loc_x_y_a_b(dataframe):
    assert isinstance(dataframe.iloc[0:1, 0:1], DataFrame) == True


@pytest.fixture
def groupby_dataframe():
    return read_csv("files/group_by_test.csv")


def test_df_groupbby_agg_type(groupby_dataframe):
    with pytest.raises(TypeError):
        groupby_dataframe.groupby(by = "fhk", agg = {"gfbb", print})


def test_df_groupbby_agg_keys_type(groupby_dataframe):
    with pytest.raises(TypeError):
        groupby_dataframe.groupby(by = "fhk", agg = {3 : print})


def test_df_groupbby_agg_keys_value(groupby_dataframe):
    with pytest.raises(ValueError):
        groupby_dataframe.groupby(by = "fhk", agg = {"gfbb" : print})


def test_df_groupbby_by_type(groupby_dataframe):
    with pytest.raises(TypeError):
        groupby_dataframe.groupby(by = 3, agg = {"DEPTNAME" : print})


def test_df_groupbby_by_value(groupby_dataframe):
    with pytest.raises(ValueError):
        groupby_dataframe.groupby(by = "fdhkvbfdkb", agg = {"DEPTNAME" : print})



    # # Vérification de la méthode groupby
    # right = dataframe.read_csv("files/group_by_test.csv")
    # right.print_as_table()
    # print ("-----")
    # # agg : TypeError
    # # right.groupby(by = "fhk", agg = {"gfbb", print})
    # # agg.keys() : TypeError
    # # right.groupby(by = "fhk", agg = {3 : print})
    # # agg.keys() : ValueError
    # # right.groupby(by = "fhk", agg = {"gfbb" : print})
    # # by : TypeError
    # # right.groupby(by = 3, agg = {"DEPTNAME" : print})
    # # by : ValueError
    # # right.groupby(by = "fdhkvbfdkb", agg = {"DEPTNAME" : print})
    # # groupby OK for a single value
    # # right.groupby(by = "DEPTNAME", agg = {"DEPTID" : max}).print_as_table()
    # # groupby OK
    # right.groupby(by = ["DEPTNAME", "LOCATION"], agg = {"DEPTID" : max}).print_as_table()