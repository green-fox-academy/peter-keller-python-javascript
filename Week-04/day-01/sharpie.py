class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = float(width)
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1

sharpie = Sharpie("green", 3.2)
sharpie2 = Sharpie("blue", 1.1)
sharpie3 = Sharpie("yellow", 1.4)
sharpie4 = Sharpie("pink", 2.0)
#print(sharpie.color, sharpie.width, sharpie.ink_amount)
sharpie.use()
#print(sharpie.color, sharpie.width, sharpie.ink_amount)