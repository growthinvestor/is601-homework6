import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'SubtractCommand initialized with a={a} and b={b}')

    def execute(self):
        logging.debug('Executing SubtractCommand')
        result = self.a - self.b
        logging.info(f'Calculated {self.a} minus {self.b}, result: {result}')
        return result

def register():
    return SubtractCommand
