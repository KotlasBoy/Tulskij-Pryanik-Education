user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text=' +  '%20'.join(user_query.split())

print(url)