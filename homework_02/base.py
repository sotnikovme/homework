from abc import ABC, abstractmethod
from homework_02.exceptions import NotEnoughFuel, LowFuelError
# from homework_02 import exceptions
# from exceptions import NotEnoughFuel, LowFuelError

# @abstractmethod
class Vehicle(ABC):
    weight=1000
    started=False
    fuel=30
    fuel_consumption=5
    def __init__(self, weight=1000, fuel=30, fuel_consumption=5):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption


    # @abstractmethod
    # def __init__(self, weight, fuel, fuel_consumption):
    #     self.weight=weight
    #     self.fuel=fuel
    #     self.fuel_consumption=fuel_consumption

    def move(self, size):
        result = self.fuel - size * self.fuel_consumption
        if result < 0:
            # exceptions.NotEnoughFuel
            raise NotEnoughFuel
            print("Error") 
        else:
            self.fuel=result
            return self.fuel
             



    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True

            else: 
                raise LowFuelError
                print('Error')
        return self