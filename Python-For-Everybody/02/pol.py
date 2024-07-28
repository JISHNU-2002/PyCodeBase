class car:
	print("POLYMORPHISM\n------------")
	items = []
	def __init__(self,items):
		self.items = items
		
	def __add__(self,other):
		return car(self.items + other.items)
	def print(self):
		print(self.items)
		
car1 = car(["HONDA","HYUNDAI"])
car2 = car(["TOYOTA","FORD"])
car3 = car1 + car2
car3.print() 

class departement():
	print("ENCAPSULATION\n------------")
	def __init__(self):
		self.id = 31
cse = departement() 
