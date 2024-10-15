import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logging.debug(f'AddCommand initialized with a={a} and b={b}')
    
    def execute(self):
        logging.debug('Executing AddCommand')
        result = self.a + self.b
        logging.info(f'Calculated {self.a} plus {self.b}, result: {result}')
        return result

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

class ExponentiateCommand(Command):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
        logging.debug(f'ExponentiateCommand initialized with base={base} and exponent={exponent}')

    def execute(self):
        logging.debug('Executing ExponentiateCommand')
        result = self.base ** self.exponent
        logging.info(f'Calculated {self.base} raised to the power of {self.exponent}, result: {result}')
        return result
