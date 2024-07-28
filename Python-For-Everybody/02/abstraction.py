from abc import ABC, abstractmethod

class Parent():
    def parent():
        print("Hello World")
        
    @abstractmethod
    def getName(self):
        pass
        
    @abstractmethod
    def getAge(self):
        pass
        
class First(Parent):
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def getName(self):
        print(self.fname + " " +self.lname)
        
    def getAge(self):
        print(self.age)
        
class Second(Parent):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)
        
obj = First("Jishnu", "J S", 21)
obj.getName()
obj.getAge()

obj = Second("Vishnu J S", 19)
obj.getName()
obj.getAge()
