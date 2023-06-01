import pytest
from src.MyBear.series import Series, list_to_int_or_float


@pytest.fixture
def serie():
    return Series("column", [1, 2, 3])


@pytest
def serie_is_serie_class(serie):
    assert isinstance(serie, Series) == True


def serie_values(serie):
    assert serie.values == [1, 2, 3]


def serie_max(serie):
    assert serie.max == 3


def serie_min(serie):
    assert serie.min == 1


def serie_std(serie):
    assert serie.std == 1  # TO DO


def serie_mean(serie):
    assert serie.mean == 2


def serie_count(serie):
    assert serie.count == 3


def serie_missing(serie):
    assert serie.missing == 0


def serie_type(serie):
    assert isinstance(serie.type, int) == True


@pytest.mark.parametrize(
    "value, expected",
    [
        (["1"], [1]),
        ([5], [5]),
        (["25.8"], [25.8]),
        (["hello"], ["hello"]),
        ([1, "2", "3.5"], [1, 2, 3.5]),
    ],
)
def serie_list_to_int_or_float(value, expected):
    assert list_to_int_or_float(value) == expected
