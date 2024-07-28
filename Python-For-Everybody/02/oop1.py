class car:
	"""DOCUMENTATION SECTION"""
	print("CAR SECTION\n"+"-----------\n")
	wheels=4
	objects=0
	
	def __init__(self,model,brand,year):
		self.model=model
		self.brand=brand
		self.year=year
		car.objects+=1
	
	def start(self):
		print('model no : ',self.model+'\n'+'brand    : ',self.brand+'\n'+'year     : ',self.year)
		print('objectno : ',car.objects)
		
	def emergency(self,airbag):
		if(airbag):
			print('Airbag present\n')
		else:
			print('No airbag present\n')
		
		
car.__doc__

crv = car('001','honda',2017)
crv.start()
crv.emergency(airbag=True)
crv.__dict__

corolla = car('002','hundai',2019)
corolla.start()
corolla.emergency(airbag=False)
corolla.__dict__


class bike:
	"""DOCS SECTOR"""
	print("BIKE SECTION\n"+"------------\n")
	wheel=2
	objectq=0
	
	def __init__(self,model,brand,year):
		self.model=model
		self.brand=brand
		self.year=year
		
	def race(self):
		print('model no : ',self.model+'\n'+'brand    : ',self.brand+'\n'+'year     : ',self.year)
	
	def brake(self,disc):
		bike.objectq+=1
		print('objectno : ',bike.objectq)
		if(disc):
			print("Disc brake present\n")
		else:
			print("No disc brake present\n")
	
bike.__doc__

mahindra = bike('01','centuro',2014)
mahindra.race()
mahindra.brake(disc=False)
mahindra.__dict__

duke = bike('10','ktm',2016)
duke.race()
duke.brake(disc=True)
duke.__dict__
		
class cycle(bike):
	"""doc SECTION"""
	print('CYCLE SECTION\n'+'-------------\n')
	def __init__(self,model,brand,year,gear):
		self.gear=gear
		super().__init__(model,brand,year)
		
	def begin(self):
		super().race()
		print('nof gear :  '+self.gear)
		
	def brake(self,disc):
		if(disc):
			print('Gear and Disc brake\n')
		else:
			print('Gear and without Disc brake\n')
		
cycle.__doc__

rocky = cycle('3.0','herculies',2017,'6')
rocky.begin()
rocky.brake(disc=True)
rocky.__dict__

hero = cycle('2.0','rally',1999,'5')
hero.begin()
hero.brake(disc=False)
hero.__dict__	


