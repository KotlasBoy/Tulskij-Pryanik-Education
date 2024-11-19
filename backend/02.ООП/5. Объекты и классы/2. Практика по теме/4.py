class BacteriaProducer:
    # Допишите инициализатор класса 
    def __init__(self, max_population_value):
        self.max_population_value = max_population_value
        self.current_population_value = 0
        

    # Допишите метод
    def create_new(self):
        if self.current_population_value < self.max_population_value:
            self.current_population_value += 1
            print(f'Добавлена одна бактерия. Количество бактерий в популяции: {self.current_population_value}')
        else:
            print('Нет места под новую бактерию')

    # Допишите метод
    def remove_one(self):
        if self.current_population_value > 0:
            self.current_population_value -= 1
            print(f'Одна бактерия удалена. Количество бактерий в популяции: {self.current_population_value}')
        else:
            print('В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_population_value=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()