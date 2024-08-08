class A:
    def __init__(self):
        self.name = "Jishnu"
        self.age = 21
        
    def getAttr(self):
        print(self.name, self.age)
            
class B:
    def __init__(self):
        self.name = "Vishnu"
        self.age = 19
        
    def getAttr(self):
        print(self.name, self.age)
        
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        
    def getAttr(self):
        print(self.name, self.age)
        
obj = C()
obj.getAttr()
