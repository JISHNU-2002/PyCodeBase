class Circle:
    def __init__(self, radius):    # constructor
        self.__radius = radius     # private attribute

    def get_radius(self):          # accessor
        return self.__radius

    def set_radius(self, radius):  # mutator
        self.__radius = radius
        
circle = Circle(5)
print(circle.get_radius())  # 5
circle.set_radius(10)
print(circle.get_radius())  # 10
