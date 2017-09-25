class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = float(width)
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

sharpie = Sharpie("green", 3.2)
print(sharpie.color, sharpie.width, sharpie.ink_amount)
sharpie.use()
print(sharpie.color, sharpie.width, sharpie.ink_amount)