from random import randint as rnd


def get_dumplings_recommendation():
    return rnd(10, 20)


# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
print(f'Оптимальным количеством пельменей на сегодня будет {get_dumplings_recommendation()}')