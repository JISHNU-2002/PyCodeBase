class Person:
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name
        
    def isEmp(self):
        return False
        
class Emp(Person):
    def isEmp(self):
        return True
        
obj = Person("Jishnu")
print(obj.getName(), obj.isEmp())

e = Emp("Vishnu")
print(e.getName(), e.isEmp())

