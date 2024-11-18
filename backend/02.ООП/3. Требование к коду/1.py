from math import *


def add_numbers(x, y):
    return x + y


def CalculateSquareRoot(Number):
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    return f"Мы вычислили квадратный корень из введённого вами числа. Это будет: {CalculateSquareRoot(your_number)}"


x = 10
y = 5

print('Сумма чисел: ', add_numbers(x, y))

print(calc(25.5))
