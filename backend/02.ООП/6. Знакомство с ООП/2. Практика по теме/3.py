class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_info(self):
        return f"{self.name} (в наличии: {self.quantity})"

class Kettlebell(Product):
    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        self.weight = weight

    def get_weight(self):
        info = self.get_info()
        return f"{info}. Вес: {self.weight} кг"

class Clothing(Product):
    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size

    def get_size(self):
        info = self.get_info()
        return f"{info}. Размер: {self.size}"

# Пример использования классов
kettlebell = Kettlebell("Гиря детская", 12, 0.75)
print(kettlebell.get_weight())  # Гиря детская (в наличии: 12). Вес: 0.75 кг

clothing = Clothing("Шляпа с рукавами", 3, "XXL")
print(clothing.get_size())  # Шляпа с рукавами (в наличии: 3). Размер: XXL
