def get_stickers_comparison(collection_1, collection_2):
    # Преобразуем коллекции в множества для удобства работы с уникальными элементами
    set_1 = set(collection_1)
    set_2 = set(collection_2)

    # Уникальные стикеры из collection_1
    unique_in_collection_1 = sorted(list(set_1 - set_2))

    # Уникальные стикеры из collection_2
    unique_in_collection_2 = sorted(list(set_2 - set_1))

    # Стикеры, которые есть в обоих коллекциях
    common_stickers = sorted(list(set_1 & set_2))

    return (unique_in_collection_1, unique_in_collection_2, common_stickers)

# Списки стикеров:
stas_collection = ['Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс', 'Линус Торвальдс', 'Маргарет Гамильтон', 'Бьярн Страуструп']
anton_collection = ['Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс', 'Бьярн Страуструп', 'Бьярн Страуструп', 'Кен Томпсон', 'Деннис Ричи']

# Вызываем функцию и распаковываем полученный кортеж в три переменные:
stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(stas_collection, anton_collection)
# Печатаем результаты:
print('Стикеры, которые есть только у Стаса:', stas_stickers)
print('Стикеры, которые есть только у Антона:', anton_stickers)
print('Стикеры, которые есть и у Стаса, и у Антона:', common_stickers)