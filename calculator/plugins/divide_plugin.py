import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'DivideCommand initialized with a={a} and b={b}')

    def execute(self):
        logging.debug('Executing DivideCommand')
        if self.b == 0:
            logging.error('Attempted to divide by zero')
            return "Cannot divide by zero!"
        result = self.a / self.b
        logging.info(f'Divided {self.a} by {self.b}, result: {result}')
        return result

def register():
    return DivideCommand