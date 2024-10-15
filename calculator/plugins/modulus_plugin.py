import logging
from calculator.commands import Command

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ModulusCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'ModulusCommand initialized with a={a} and b={b}')

    def execute(self):
        logging.debug('Executing ModulusCommand')
        if self.b == 0:
            logging.error('Attempted to perform modulus by zero')
            return "Cannot perform modulus by zero!"
        result = self.a % self.b
        logging.info(f'Calculated {self.a} modulus {self.b}, result: {result}')
        return result

def register():
    return ModulusCommand
