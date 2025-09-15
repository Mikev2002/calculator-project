import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.test_calc import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

