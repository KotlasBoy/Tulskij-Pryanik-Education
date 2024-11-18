# Пропишите нужные импорты.
from datetime import datetime, time, timedelta

# Напишите код функции, следуя плану из задания.
def get_results(time_leader_str, time_member_str):
    time_leader = datetime.strptime(time_leader_str, "%H:%M:%S")
    time_member = datetime.strptime(time_member_str, "%H:%M:%S")
    delta = time_member - time_leader
    if time_leader_str != time_member_str:
        print(f"Вы пробежали за {time_member_str} с отставанием от лидера {delta}")
    else:
        print(f"Вы пробежали за {time_leader_str} и победили!")
# Проверьте работу программы, можете подставить свои значения.
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')