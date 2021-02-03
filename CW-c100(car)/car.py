class Car(object):
    def __init__(self, brand, colour, fuelType, mileage=None ):
        self.brand = brand
        self.colour = colour
        self.fuelType = fuelType
        self.mileage = mileage

    def setModel(self, model, brand):
        self.brand[model] = brand
    def Getmodel(self, model):
       return self.brand[model] 
