from Aircraft import Aircraft

class Carrier:
    def __init__(self, store_of_ammo, health_point):
        self.list_of_aircraft = []
        self.store_of_ammo = store_of_ammo
        self.health_point = health_point

    def addAircraft(self, aircraft):
        self.list_of_aircraft.append(aircraft)

    def fill(self):
        for item in self.list_of_aircraft:
            if item.getType() == "F35":
                self.store_of_ammo = item.refill(self.store_of_ammo)
                print(str(self.store_of_ammo))

    def fight(self, Carrier):
        carrier_max_dmg = 0
        for item in self.list_of_aircraft:
            carrier_max_dmg += 

carrier = Carrier(1000, 2000)

aircraft1 = Aircraft("F35")
carrier.addAircraft(aircraft1)
aircraft2 = Aircraft("F16")
carrier.addAircraft(aircraft2)
aircraft3 = Aircraft("F35")
carrier.addAircraft(aircraft3)
aircraft4 = Aircraft("F16")
carrier.addAircraft(aircraft4)
aircraft5 = Aircraft("F35")
carrier.addAircraft(aircraft5)
aircraft6 = Aircraft("F16")
carrier.addAircraft(aircraft6)