import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

DATE_FORMAT = '%Y-%m-%d'


def add(items, title: str, amount: Decimal, expiration_date_str: str = None):
    if expiration_date_str is not None:
        expiration_date = (datetime.datetime.strptime(expiration_date_str, DATE_FORMAT)).date()
    else:
        expiration_date = None
    if title in items:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    note_list = note.split()
    if '-' in note_list[-1]:
        expiration_date_str = note.split()[-1]
        amount = Decimal(note_list[-2])
        title = ' '.join(note_list[:-2])
    else:
        expiration_date_str = None
        amount = Decimal(note_list[-1])
        title = ' '.join(note_list[:-1])

    add(items, title, amount, expiration_date_str)


def find(items, needle):
    list_of_finding = []
    for title in items:
        if needle.lower() in title.lower():
            list_of_finding.append(title)
    return list_of_finding


def amount(items, needle):
    list_of_finding = find(items, needle)
    counter = Decimal("0")
    for title in list_of_finding:
        for d in items[title]:
            counter += d['amount']
    return counter


def expire(items, in_advance_days=0):
    today = datetime.date.today()
    exit_list = []
    expire_day = today + datetime.timedelta(days=in_advance_days)
    for title in items:
        counter = Decimal('0')
        for d in items[title]:
            if d['expiration_date'] is not None:
                if d['expiration_date'] <= expire_day:
                    counter += d['amount']
        if counter > Decimal('0'):
            exit_list.append((title, counter))
    return exit_list


