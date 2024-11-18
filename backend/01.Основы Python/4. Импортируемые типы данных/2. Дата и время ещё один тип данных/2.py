# Допишите нужные импорты.
from datetime import datetime, timedelta

def timedelta_days(datetime_str_1, datetime_str_2):
    datetime_1= datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
    datetime_2= datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')
    return (datetime_2 - datetime_1).days

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')