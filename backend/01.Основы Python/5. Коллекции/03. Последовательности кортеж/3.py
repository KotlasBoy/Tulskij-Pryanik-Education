def assess_yield(number_of_plants, average_weight):
    weight = float(number_of_plants * average_weight) / 1000
    if weight > 100:
        return (weight, 'Ожидается отличный урожай.')
    elif weight > 50:
        return (weight, 'Ожидается хороший урожай.')
    elif weight > 0:
        return (weight, 'Урожай будет так себе.')
    else:
        return (weight, 'Урожая не будет.')
# Пример вызова функции
total_weight, rating = assess_yield(50, 200)
print(total_weight, 'кг.', rating)








