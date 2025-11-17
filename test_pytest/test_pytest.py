from main import custom_sum


def test_plus():
    assert 1 + 2 == 3


def test_minus():
    assert 1 - 2 == -1


def test_sum1():
    assert 19.2 == custom_sum([1, 9.2, 9])


def test_sum():
    assert 19.2 == custom_sum([1, 9.2, 9])
