from sharpie import Sharpie 

class SharpieSet(object):
    def __init__(self):
        self.sharpie = [Sharpie("blue", 1.1), Sharpie("yellow", 1.4)]

    def count_usable(self):
        for i in range(0,1):
            if self.sharpie[i].ink_amount > 0:
                usable_sharpies += 1

    def remove_trash(self):
        for i in range(0,1):
            if self.sharpie[i].ink_amount <= 0:
                self.sharpie.remove(self.sharpie[i])

sharpie_list = SharpieSet()

sharpie_list.sharpie[0].use()
sharpie_list.sharpie[0].use()
sharpie_list.sharpie[0].use()
sharpie_list.sharpie[0].use()
print(sharpie_list.sharpie[0].ink_amount)

sharpie_list.remove_trash()
print(sharpie_list.sharpie[0])

