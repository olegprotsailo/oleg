class Car():
    def __init__(self,name):
        self.name=name
    def fullname(self):
        print(self.name)

class ElectroCar(Car):
    def __init__(self,name):
        super().__init__(name)
    def fullname(self):
        print("Tesla")
mytesla=ElectroCar("Lambo")
print(mytesla.fullname())
