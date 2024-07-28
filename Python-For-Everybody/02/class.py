class car(object):
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color
        self.owners=0

    def carinfo(self):
        print(self.make)
        print(self.model)
        print(self.color)
        print(self.owners)

    def sell(self):
        self.owners=self.owners+1

car1 = car("honda","v1","black")
car1.sell()
car1.carinfo()
car2 = car(make="suzuki",model="v2",color="white")
car2.sell()
car2.sell()
car2.carinfo()
car3 = car(model="v3",make="toyota",color="silver")
car3.sell()
car3.sell()
car3.sell()
car3.carinfo()