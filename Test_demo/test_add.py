import time
import pytest



@pytest.mark.parametrize("x,y",[
    (3+5, 9),
    (2+4, 6),
    (6*9, 54),
])


def test_1(x,y):
    assert x == y

# def add(x,y):
#     return x + y
#
# def test_add():
#     assert add(1,2) == 3
#
# def test_add1():
#     time.sleep(10)
#     assert add(3,3) == 6

# class Test_add():
