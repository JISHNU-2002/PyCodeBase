class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car: {self.brand} {self.model}"
        
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Mahindra", "Thar")
print(my_car1.display())
print(my_car2.display())
