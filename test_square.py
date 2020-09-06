import pytest

def square(x):
    return x ** 2

@pytest.mark.parametrize("x, x2", [(0, 0), (1, 1), (2, 4), (3, 9)])
def test_square(x, x2):
    return square(x) == x2

print(test_square())