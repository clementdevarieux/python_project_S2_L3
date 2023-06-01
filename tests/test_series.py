import pytest
from src.MyBear.series import Series


@pytest.fixture
def serie():
    return Series("column", [1, 2, 3])


def test_serie_is_serie_class(serie):
    assert isinstance(serie, Series) == True


def test_serie_values(serie):
    assert serie.values == [1, 2, 3]


def test_serie_max(serie):
    assert serie.max == 3


def test_serie_min(serie):
    assert serie.min == 1


def test_serie_std(serie):
    assert serie.std == 0.8165


def test_serie_mean(serie):
    assert serie.mean == 2


def test_serie_count(serie):
    assert serie.count == 3


def test_serie_missing(serie):
    assert serie.missing == 0


def test_serie_type(serie):
    assert serie.type == int


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
def test_serie_list_to_int_or_float(value, expected, serie):
    assert serie.list_to_int_or_float(value) == expected
