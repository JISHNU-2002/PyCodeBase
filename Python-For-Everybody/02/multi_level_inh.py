class First:
    def first(self):
        print("I am the first class")

class Second(First):
    def second(self):
        print("I am the second class")
        
class Third(Second):
    def third(self):
        print("I am the third class")
        
obj = Third()
obj.third()
obj.second()
obj.first()
