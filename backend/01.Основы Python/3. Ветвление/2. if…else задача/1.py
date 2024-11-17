def get_season(month):
    if month == 'декабрь' or month == 'январь' or month == 'февраль':
        return 'зима'
    elif month == 'март' or month == 'апрель' or month == 'май':
        return 'весна'
    elif month == 'июнь' or month == 'июль' or month == 'август':
        return 'лето'
    elif month == 'сентябрь' or month == 'октябрь' or month == 'ноябрь':
        return 'осень'
    else:
        return 'Ошибка в написании месяца!'

# Для контроля вызовем функцию и напечатаем результат.
print(get_season('июнь'))  # лето
print(get_season('мартобрь'))  # Ошибка в написании месяца!
