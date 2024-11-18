num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

# Преобразуем строки в множества чисел
set_1 = set(map(int, num_string_1.split()))
set_2 = set(map(int, num_string_2.split()))

# Найдем пересечение множеств
common_numbers = set_1.intersection(set_2)

# Выведем количество одинаковых чисел
print(len(common_numbers))
