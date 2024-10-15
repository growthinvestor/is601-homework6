'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide, modulus, exponentiate 


def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()

def test_operation_modulus():
    '''Testing the modulus operation'''
    calculation = Calculation(Decimal('10'), Decimal('3'), modulus)
    assert calculation.perform() == Decimal('1'), "Modulus operation failed"

def test_operation_exponentiation():
    '''Testing the exponentiation operation'''
    calculation = Calculation(Decimal('2'), Decimal('3'), exponentiate)
    assert calculation.perform() == Decimal('8'), "Exponentiation operation failed"
    