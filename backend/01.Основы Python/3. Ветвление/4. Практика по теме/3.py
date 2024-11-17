def find_pool_capacity(num_of_people, length, width=None):
    # Преобразуем отрицательные значения в положительные
    num_of_people = abs(num_of_people)
    length = abs(length)

    # Обрабатываем ширину бассейна
    if width is None:
        width = length
    else:
        width = abs(width)

    # Вычисляем площадь бассейна
    pool_area = length * width

    # Вычисляем максимальное количество людей, которое может поместиться в бассейн
    max_people = pool_area * 2

    # Проверяем, помещаются ли люди в бассейн
    if num_of_people <= max_people:
        print(f"Бассейн площадью {pool_area} кв. м. вмещает {num_of_people} чел.")
    else:
        print(f"Бассейн площадью {pool_area} кв. м. не вмещает {num_of_people} чел.")

# Проверьте работу функции, можете подставить свои значения.
find_pool_capacity(4, 2)
find_pool_capacity(4, 5, 10)
find_pool_capacity(-10, -5, -2)
