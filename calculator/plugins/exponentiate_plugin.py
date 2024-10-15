import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ExponentiateCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'ExponentiateCommand initialized with a={a} and b={b}')

    def execute(self):
        logging.debug('Executing ExponentiateCommand')
        result = self.a ** self.b
        logging.info(f'Calculated {self.a} raised to the power of {self.b}, result: {result}')
        return result

def register():
    return ExponentiateCommand
