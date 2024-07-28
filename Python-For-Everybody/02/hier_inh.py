class Parent:
    def parent(self):
        print("I am parent class")

class First(Parent):
    def first(self):
        print("I am child1")
        
class Second(Parent):
    def second(self):
        print("I am child2")
        
obj1 = First()
obj2 = Second()
obj1.parent()
obj1.first()
obj2.parent()
obj2.second()

