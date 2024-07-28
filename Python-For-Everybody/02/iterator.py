# iterable - string, list, tuple etc

t = ("car", "bike", "train")
myiter = iter(t)

for i in range(len(t)):
    print(next(myiter))
    
s = "this is a string"
myiter = iter(s)
for i in range(len(s)):
    print(next(myiter))

class Iterator:
    def __iter__(self):
        self.a = 1
        return self
        
    def __next__(self):
        x = self.a
        self.a+=1
        return x
        
obj = Iterator()
myiter = iter(obj)

for i in range(10):
    print(next(myiter))

names = input("comma-separated names : ")
names = names.title().split(",")
print(names)
myiter = iter(names)
for i in range(len(names)):
    print(next(myiter))
