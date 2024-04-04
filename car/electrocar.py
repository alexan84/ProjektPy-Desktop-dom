# from car import carclass
from car.carclass import CarClass

class ElectroCar(CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100
    def description_battery(self):
        print(f'мощность заряда автомобиля {self.battery}%')