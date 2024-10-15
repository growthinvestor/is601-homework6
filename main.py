from dotenv import load_dotenv
import os
import logging
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, ModulusCommand, ExponentiateCommand

# Load environment variables from .env file
load_dotenv()

# Set up logging
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
valid_log_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

# Ensure the log level is valid
if log_level not in valid_log_levels:
    log_level = "INFO"  # fallback to default

log_directory = "logs"
log_file = os.path.join(log_directory, "app.log")

# Create log directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

# Create a file handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(log_level)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Console can log debug messages
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def calculate_and_print(a_string=None, b_string=None, operation_string=None):
    calc = Calculator()

    if a_string is not None and b_string is not None and operation_string is not None:
        try:
            a = float(a_string)
            b = float(b_string)

            # Logging input and operation
            logger.debug(f"Received inputs: a={a}, b={b}, operation={operation_string}")

            # Creating commands based on the operation
            if operation_string == 'add':
                calc.load_plugin('add_plugin')
                command = AddCommand(a, b)
            elif operation_string == 'subtract':
                command = SubtractCommand(a, b)
            elif operation_string == 'multiply':
                calc.load_plugin('multiply_plugin')
                command = calc.create_command('multiply_plugin', a, b)
            elif operation_string == 'divide':
                if b == 0:
                    logger.error("Attempted to divide by zero.")
                    print("An error occurred: Cannot divide by zero.")
                    return
                calc.load_plugin('divide_plugin')
                command = calc.create_command('divide_plugin', a, b)
            elif operation_string == 'modulus':
                command = ModulusCommand(a, b)
            elif operation_string == 'exponentiate':
                command = ExponentiateCommand(a, b)
            else:
                logger.error(f"Unknown operation: {operation_string}")
                print(f"Unknown operation: {operation_string}.")
                return

            result = calc.compute(command)
            result_str = str(int(result)) if result.is_integer() else str(result)

            logger.info(f"Calculation result: {result_str}")
            print(f"The result of {a} {operation_string} {b} is equal to {result_str}.")

        except ValueError:
            logger.error(f"Invalid input: {a_string} or {b_string} is not a valid number.")
            print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
    else:
        while True:
            print("\nOptions:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply (using plugin)")
            print("4. Divide (using plugin)")
            print("5. Modulus")
            print("6. Exponentiate")
            print("7. Exit")

            choice = input("Choose an option (1-7): ")

            if choice == '7':
                logger.info("User chose to exit the program.")
                print("Exiting the calculator. Goodbye!")
                break

            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
            except ValueError:
                logger.error("Invalid number input.")
                print("Invalid number input.")
                continue

            # Mapping choices to commands
            command = None
            if choice == '1':
                command = AddCommand(a, b)
            elif choice == '2':
                command = SubtractCommand(a, b)
            elif choice == '3':
                calc.load_plugin('multiply_plugin')
                command = calc.create_command('multiply_plugin', a, b)
            elif choice == '4':
                if b == 0:
                    logger.error("Attempted to divide by zero.")
                    print("An error occurred: Cannot divide by zero.")
                    continue
                calc.load_plugin('divide_plugin')
                command = calc.create_command('divide_plugin', a, b)
            elif choice == '5':
                command = ModulusCommand(a, b)
            elif choice == '6':
                command = ExponentiateCommand(a, b)
            else:
                logger.warning(f"Invalid choice: {choice}")
                print("Invalid choice. Please select a valid option.")
                continue

            # Compute result and log it
            if command is not None:
                result = calc.compute(command)
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                logger.info(f"Result of the operation: {result_str}")
                print(f"Result: {result_str}")

if __name__ == "__main__":
    logger.debug("Program started.")
    calculate_and_print()
