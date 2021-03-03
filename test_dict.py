import pytest


@pytest.mark.parametrize("dict, value, expected", [({'Name': 'Masha', 'Age': 23, 'Course': 'Accounting'}, 'Name', 'Masha'),
                                                   ({1: 'Masha', 2: 23, 3: 'Accounting'}, 2, 23)])
def test_read(dict, value, expected):
    assert dict[value] == expected


def test_create():
    dict = {1: 'mango', 2: 'pawpaw'}
    assert dict == {1: 'mango', 2: 'pawpaw'}


def test_error_read():
    try:
        dict = {1: 'mango', 2: 'pawpaw'}
        a = dict[1]
        assert a == 'pawpaw'
    except AssertionError:
        pass

