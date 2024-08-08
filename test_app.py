# test_app.py

import pytest
from app import addition, division ,multiplication, soustraction

def test_add():
    assert addition(10, 5) == 15
    assert addition(-1, 1) == 0
    assert addition(-1, -1) == -2

def test_subtract():
    assert soustraction(10, 5) == 5
    assert soustraction(-1, 1) == -2
    assert soustraction(-1, -1) == 0

def test_multiply():
    assert multiplication(10, 5) == 50
    assert multiplication(-1, 1) == -1
    assert multiplication(-1, -1) == 1

def test_divide():
    assert division(10, 5) == 2.0
    assert division(-1, 1) == -1.0
    assert division(-1, -1) == 1.0

if __name__ == "__main__":
    pytest.main()
