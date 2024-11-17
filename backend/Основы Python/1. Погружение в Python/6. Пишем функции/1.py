def get_rectangle_area(a, b):
    return a * b


def get_rectangle_perimeter(a, b):
        return 2 * (a + b)


# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10

print(f'Площадь: {get_rectangle_area(length, width)}')
print(f'Периметр: {get_rectangle_perimeter(length, width)}')