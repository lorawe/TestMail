import pytest


@pytest.mark.parametrize("first_set, test_input, expected", [({1, 2}, 1, {1, 2}),
                                                             ({1, 2}, 1.02, {1, 2, 1.02}),
                                                             ({"first_string"}, "second_string",
                                                              {"first_string", "second_string"})])
def test_adding(first_set, test_input, expected):
    first_set.add(test_input)
    assert first_set == expected


def test_create():
    a = {1, 2, 3}
    assert a == {1, 2, 3}


def test_error_adding():
    try:
        a = {1, 2, 4}
        a.add(3)
        assert a == {1, 2, 3, 4, 5}
    except AssertionError:
        pass

