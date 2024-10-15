import pytest
from main import calculate_and_print  # Ensure this import is correct

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5.0 add 3.0 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10.0 subtract 2.0 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4.0 multiply 5.0 is equal to 20"),
    ("20", "4", 'divide', "The result of 20.0 divide 4.0 is equal to 5"),
    ("1", "1", 'divide', "The result of 1.0 divide 1.0 is equal to 1"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero."),
    ("9", "3", 'modulus', "The result of 9.0 modulus 3.0 is equal to 0"),
    ("10", "3", 'modulus', "The result of 10.0 modulus 3.0 is equal to 1"),
    ("2", "3", 'exponentiate', "The result of 2.0 exponentiate 3.0 is equal to 8"),
    ("3", "0", 'exponentiate', "The result of 3.0 exponentiate 0.0 is equal to 1"),
    ("9", "3", 'unknown', "Unknown operation: unknown."),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_main(a_string, b_string, operation_string, expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    
    # Capture the output
    captured = capsys.readouterr().out.strip().rstrip(".")
    
    # Convert any floats that look like integers to ints in the string
    captured = captured.replace('.0', '')
    expected_string = expected_string.rstrip(".").replace('.0', '')
    
    assert captured == expected_string
