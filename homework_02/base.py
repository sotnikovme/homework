from abc import ABC, abstractmethod
from exceptions import NotEnoughFuel, LowFuelError

# @abstractmethod
class Vehicle(ABC):
    def __init__(self, weight=1000, started=True, fuel=30, fuel_consumption=5):
        self.weight=weight
        self.started=started
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
               exceptions.NotEnoughFuel
               print("Error") 
        else:
            self.fuel=result
            return self.fuel
             



    def start(self, started):
        if self.started == False:
            if self.fuel > 0:
                self.started = True

            else: 
                exceptions.LowFuelError
                print('Error')
        return self