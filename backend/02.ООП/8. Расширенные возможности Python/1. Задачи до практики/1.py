# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
generator = (digit ** 2 for digit in numbers if digit % 3 == 0)

# Распечатайте сумму квадратов.
print(sum(generator))