import pytest

from sample.app import div, fact, flatten, gcd

@pytest.mark.testing_divisor
def test_div():
    assert div(20, 40) == [21, 28], "Your div function does not seem to be working"

@pytest.mark.testing_factorial
def test_fact():
     assert fact(5) == 120, "Your fact function does not seem to be working"

@pytest.mark.testing_flatten_list
def test_flatten():
     assert flatten([[1, 2], 3, [4], 5, [6, 7], [[],[]]]) == [1, 2, 3, 4, 5, 6, 7], "Your flatten function does not seem to be working"

@pytest.mark.testing_greatest_common_divisor
def test_gcd():
     assert gcd([43023, 393, 8373, 445, 66,5, 900, 32323, 452534, 59945]) == 1, "Your gcd function does not seem to be working"