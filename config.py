from operator import add, mul, truediv, sub
from math import cos, sin, tan, log, sqrt

BUTTONS = [f'btn_{num}' for num in range(0, 10)]
ERROR_ZERO_DIV = 'Division by zero'
ERROR_UNDEFINED = 'Result is undefined'

OPERATIONS = {
    "+": add,
    "-": sub,
    "÷": truediv,
    "×": mul
}

TRIGONOMETRIC_OPERATIONS = {
    "ln": log,
    "√": sqrt,
    "tan": tan,
    "cos": cos,
    "sin": sin
}


