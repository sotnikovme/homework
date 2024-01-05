# from homework_02.base import Vehicle
from exceptions import CargoOverload
from base import Vehicle

class Plane(Vehicle):
    def __init__(self, cargo, max_cargo, weight, started, fuel, fuel_consumption):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, dop_cargo):
        if self.max_cargo > self.cargo + dop_cargo:
            self.cargo = self.cargo + dop_cargo
            return self.cargo
        else:
            raise CargoOverload
            print("Перегруз")

    def remove_all_cargo(self):
        new_cargo = self.cargo
        self.cargo = 0
        return new_cargo
    # yield Plane.cargo
# Plane.cargo = 0