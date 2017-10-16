class Plant(object):
    def __init__(self):
        self.abs_rate = 0
        self.need_limit = 0
        self.current_water = 0
        self.color = color
        self.type = "Plant"

    def is_need_water(self):
        return self.current_water < self.need_limit

    def watering(self, amount):
        self.current_water += amount * self.abs_rate

    def get_doesnt(self):
        return " doesn't " if not is_need_water() else " needs"

    def status(self):
        print("The " + self.color + " " + self.plant_type + self.get_doesnt() + " water.")

class Tree(Plant):
    def __init__(self, color):
        super().__init__(color)
        self.abs_rate = 0.4
        self.need_limit = 10
        self.plant_type = "Tree"

class Flower(Plant):
    def __init__(self, color):
        super().__init__(color)
        self.abs_rate = 0.75
        self.need_limit = 5
        self.plant_type = "Flower"
