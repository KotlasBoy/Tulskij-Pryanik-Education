# Импортируйте нужную библиотеку.
from datetime import datetime

class Store:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        return False

    def get_info(self, date_str):
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        
        # Передайте в метод is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату. 
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.is_open(date_object) :
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class MiniStore(Store):
    # Переопределите метод is_open().

    def is_open(self, date: datetime):
        if date.weekday() > 4:
            return False
        else:
            return True


class WeekendStore(Store):

    def is_open(self, date: datetime):
        if date.weekday() > 4:
            return True
        else:
            return False


class NonStopStore(Store):

    def is_open(self, date: datetime):
        return True
        


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))