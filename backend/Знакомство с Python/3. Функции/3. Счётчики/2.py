def number_of_occurrences(char, string):
    count = 0
    for letter in string:
        if letter == char:
            count += 1

        # Печатаем исходную строку:
    print('Исходная строка:', string)
        # Печатаем результат подсчётов:
    print('Количество вхождений символа', char, 'составляет:', count)


    # Код ниже не изменяйте
phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

    # Вызываем функцию number_of_occurrences(), чтобы она посчитала, 
    # сколько раз во фразе phrase встречается буква 'е'
number_of_occurrences('е', phrase)