from math import sqrt
from typing import Optional


def add_numbers(first: int, second: int) -> int:
    return first + second


def calculate_square_root(number: int) -> float:
    return sqrt(number)


def calc(your_number: int) -> Optional[str]:
    if your_number <= 0:
        return
    num = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {num}')


x1 = 10
y1 = 5

print('Сумма чисел: ', add_numbers(x1, y1))

print(calc(25.5))
