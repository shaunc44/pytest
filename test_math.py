from simple_math import add, subtract, multiply, divide


# test add function
def test_add_5_3():
    assert add(8, 3) == 8

def test_add_he_llo():
    assert add('he', 'llo') == 'hello'


# test subtract function
def test_subtract_20_16():
    assert subtract(20, 16) == 4

def test_subtract_decimal():
    assert subtract(6.5, 4.3) == 2.2


# test multiply function
def test_multiply_11_8():
    assert multiply(11, 8) == 88

def test_multiply_yo():
    assert multiply('yo', 2) == 'yoyo'


# test divide function
def test_divide_100_10():
    assert divide(100, 10) == 10

def test_divide_decimal():
    assert divide(0.5, 0.1) == 5