import pytest
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, ModulusCommand, ExponentiateCommand

# Fixture to set up a calculator instance before each test
@pytest.fixture
def calc():
    return Calculator()

def test_add_command(calc):
    add_command = AddCommand(10, 5)
    result = calc.compute(add_command)
    assert result == 15

def test_subtract_command(calc):
    sub_command = SubtractCommand(10, 5)
    result = calc.compute(sub_command)
    assert result == 5

def test_multiply_plugin(calc):
    # Load the multiply plugin and test it
    calc.load_plugin('multiply_plugin')
    multiply_command = calc.create_command('multiply_plugin', 10, 5)
    result = calc.compute(multiply_command)
    assert result == 50

def test_divide_plugin(calc):
    # Load the divide plugin and test it
    calc.load_plugin('divide_plugin')
    divide_command = calc.create_command('divide_plugin', 10, 5)
    result = calc.compute(divide_command)
    assert result == 2

def test_divide_by_zero(calc):
    # Test divide by zero scenario
    calc.load_plugin('divide_plugin')
    divide_command = calc.create_command('divide_plugin', 10, 0)
    result = calc.compute(divide_command)
    assert result == "Cannot divide by zero!"

def test_modulus_command(calc):
    modulus_command = ModulusCommand(10, 3)
    result = calc.compute(modulus_command)
    assert result == 1

def test_exponentiate_command(calc):
    exponentiate_command = ExponentiateCommand(2, 3)
    result = calc.compute(exponentiate_command)
    assert result == 8
