import my_app
import numpy as np

def test_case1():
    result = my_app.add_numbers(10, 5)
    assert result == 15

def test_case2():
    result = my_app.multiply_numbers(7, 5)
    assert result == 35

def test_case3():
    a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    b = 3
    result = my_app.multiply_array(a, b)
    is_equal = (result == [[3, 3, 3], [3, 3, 3], [3, 3, 3]]).all()
    assert is_equal == True