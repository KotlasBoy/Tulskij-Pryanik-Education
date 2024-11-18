# Напишите функцию get_competition_data().
def get_competition_data(data):
    set_of_teams = set('')
    exit_str = ''
    for d in data:
        for team in d:
            set_of_teams.add(team)
    for team in sorted(list(set_of_teams)):
        exit_str += f"{str(team)}, "
    print(f'Команды, участвовавшие в гонке:',exit_str[:-2])
        

races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


get_competition_data(races_data)