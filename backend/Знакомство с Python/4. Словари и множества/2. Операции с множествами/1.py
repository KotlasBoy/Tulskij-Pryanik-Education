def print_valid_cities(all_cities, used_cities):
    valid_cities = set(all_cities).difference(set(used_cities))
    for city in valid_cities:
        print(city)
    

all_cities = {
    'Абакан',
    'Астрахань', 
    'Бобруйск', 
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк', 
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}

print_valid_cities(all_cities, used_cities)