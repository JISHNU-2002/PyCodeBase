class Animal:
    def __init__(self):
        print("parent")
       
    def eat(self):
        print("parent eat")
        
class Lion(Animal):
    def eat(self):
        print("lion eat")
        
class Monkey(Animal):
    def eat(self):
        print("monkey eat")
        
lion = Lion()
monkey = Monkey()
lion.eat()
monkey.eat()
