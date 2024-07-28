class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(self.name)
        
    def showAge(self):
        print(self.age)
        
class Employee():
    def __init__(self,eid,dep):
        self.eid = eid
        self.dep = dep
        
    def getID(self):
        print(self.eid)
        
    def showDep(self):
        print(self.dep)
        
class Trainee(Person,Employee):
    def __init__(self,name,age,eid,dep):
        Person.__init__(self,name,age)
        Employee.__init__(self,eid,dep)
         
obj = Trainee("Jishnu", 21, 31, "CS")
obj.getName()
obj.showAge()
obj.getID()
obj.showDep()
