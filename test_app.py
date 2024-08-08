# test_calculs.py

from app import addition, soustraction, multiplication, division


def test_addition():
    assert addition(3, 5) == 8
    assert addition(-3, 5) == 2
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(3, 5) == -2
    assert soustraction(5, 3) == 2
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(3, 5) == 15
    assert multiplication(-3, 5) == -15
    assert multiplication(0, 5) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(5, 2) == 2.5
    assert division(8, 0) == "Erreur: Division par zéro"

