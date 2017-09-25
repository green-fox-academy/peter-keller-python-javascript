class Station():
    gas_amount = 10000


class Car():
    fuel_in_tank = 45           #this is just an example
    capacity = 100
    fuel_needed = capacity - fuel_in_tank
    def refill(self):
        Station.gas_amount -= self.fuel_needed
        Car.fuel_in_tank += self.fuel_needed

Audi = Car()
Audi.refill()
Lukoil = Station()
print(Car.fuel_in_tank)
print(Station.gas_amount)
