# Вместо многоточия укажите необходимые параметры.
def count_tiles(depth, length, width=None):
    # Опишите условие, когда ширина бассейна не указана.
    if width == None:
        width = length
    
    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
    count = depth * 2 * (length + width) + length * width

    # Верните результат работы функции.
    return count


total_tiles = count_tiles(2, 2, 2)
print('Общее количество плиток для строительства бассейна:', total_tiles)