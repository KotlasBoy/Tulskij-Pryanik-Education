# Количество корзин с овощами, шт.
baskets = 462
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175

# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(count, weight, price):
    all_weight = count * weight
    all_price = all_weight * price
    return (all_weight, all_price)

# Вызовите функцию calc() и обработайте вернувшееся значение.
tup = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f"Общий вес урожая: {tup[0]} кг. Оценённая стоимость урожая: {tup[1]}.")