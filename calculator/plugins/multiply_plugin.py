import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'MultiplyCommand initialized with a={a} and b={b}')

    def execute(self):
        logging.debug('Executing MultiplyCommand')
        result = self.a * self.b
        logging.info(f'Calculated {self.a} multiplied by {self.b}, result: {result}')
        return result

def register():
    return MultiplyCommand
