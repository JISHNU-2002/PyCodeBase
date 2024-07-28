class car(object):
    color="white"
    def __init__(self,speed,mileage):
        self.speed=speed
        self.mileage=mileage
        self.capacity=None
        
    def seating(self,capacity):
        self.capacity=capacity
        
    def info(self):
        print(self.color)
        print(self.speed)
        print(self.mileage)
        print(self.capacity)
    
car1=car(200,50000)
car1.seating(5)
car1.info()