from datetime import datetime

def validate_record(name, date_str):
    try:
        # Проверяем, соответствует ли дата формату ДД.ММ.ГГГГ
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        # Если дата не соответствует формату, выводим сообщение и возвращаем False
        print(f"Некорректный формат даты в записи: {name}, {date_str}")
        return False

def process_people(data):
    good_count = 0
    bad_count = 0

    for record in data:
        name, date_str = record
        if validate_record(name, date_str):
            good_count += 1
        else:
            bad_count += 1

    return {'good': good_count, 'bad': bad_count}

# Пример использования
data = [
    ('Акакій Башмачкинъ', '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
]

result = process_people(data)
print(f"Корректных записей: {result['good']}")
print(f"Некорректных записей: {result['bad']}")
