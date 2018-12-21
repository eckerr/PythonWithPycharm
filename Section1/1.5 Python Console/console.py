import math


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def root(a):
        return math.sqrt(a)


def greetings(name):
    print('Hello ' + name + '!')


def goodbye():
    print('Goodbye!')


myCalculator = Calculator
myCalculator.subtract(5, 3)

# execfile('console.py')
# exec('console.py')
