# Пропишите нужные импорты.
from datetime import datetime, timedelta

def get_weekday_name(weekday_number):
    if weekday_number == 0:
        return 'понедельник'
    elif weekday_number == 1:
        return 'вторник'
    elif weekday_number == 2:
        return 'среда'
    elif weekday_number == 3:
        return 'четверг'
    elif weekday_number == 4:
        return 'пятница'
    elif weekday_number == 5:
        return 'суббота'
    elif weekday_number == 6:
        return 'воскресенье'
    else:
        return 'Неверный номер дня недели'


def get_day_after_tomorrow(date_string):
    my_date = datetime.strptime(date_string, "%Y-%m-%d")
    day_after_tomorrow = my_date + timedelta(days=2)
    weekday_name = get_weekday_name(my_date.weekday())
    weekday_after_tomorrow_name = get_weekday_name(day_after_tomorrow.weekday())
    print(f'Сегодня {datetime.strftime(my_date, "%Y-%m-%d")}, {weekday_name}, а послезавтра будет {weekday_after_tomorrow_name}')


# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow('2024-01-01')
get_day_after_tomorrow('2024-01-02')
get_day_after_tomorrow('2024-01-03')
get_day_after_tomorrow('2024-01-04')
get_day_after_tomorrow('2024-01-05')
get_day_after_tomorrow('2024-01-06')