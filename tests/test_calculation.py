"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division, modulus, exponentiate) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide, modulus, exponentiate

def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(a, b, operation)  
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  

def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    
    calc1 = Calculation(Decimal('1'), Decimal('2'), add)
    calc1.perform()  
    Calculations.add_calculation(calc1)  

    calc2 = Calculation(Decimal('3'), Decimal('4'), subtract)
    calc2.perform()  
    Calculations.add_calculation(calc2)  

    add_operations = Calculations.find_by_operation("add")
    
    assert len(add_operations) >= 1, "Expected at least one addition operation in history."


def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  
    with pytest.raises(ValueError, match="Cannot divide by zero"):  
        calc.perform()

def test_modulus_operation():
    """
    Test modulus operation to ensure it works as expected.
    
    This test ensures that the modulus operation correctly returns the remainder 
    of the division of the two Decimal operands 'a' and 'b'.
    """
    calc = Calculation(Decimal('10'), Decimal('3'), modulus)  
    expected = Decimal('10') % Decimal('3')  # Expected result is 1
    assert calc.perform() == expected, f"Failed modulus operation with 10 and 3"

def test_exponentiate_operation():
    """
    Test exponentiation operation to ensure it works as expected.
    
    This test ensures that the exponentiation operation correctly returns 'a' raised
    to the power of 'b'.
    """
    calc = Calculation(Decimal('2'), Decimal('3'), exponentiate)  
    expected = Decimal('2') ** Decimal('3')  # Expected result is 8
    assert calc.perform() == expected, f"Failed exponentiation operation with 2 and 3"
