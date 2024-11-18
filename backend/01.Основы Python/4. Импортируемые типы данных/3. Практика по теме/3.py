# Пропишите нужные импорты.
from decimal import Decimal, getcontext

getcontext().prec = 3
# Напишите код функции.
def get_monthly_payment(credit, months, percent):
    credit = Decimal(str(credit))
    months = Decimal(str(months))
    percent = Decimal(str(percent))
    payment = (credit / months) * (1 + percent / 100)
    # Функция должна вернуть сумму ежемесячного платежа по кредиту.
    return payment


# Вызовите функцию get_monthly_payment() 
# с указанными в задании аргументами
# и распечатайте нужное сообщение.
print(f"Ежемесячный платёж: {get_monthly_payment(54, 24, 9)} ВтК ")