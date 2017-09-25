class Animal(object):
    
    
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
    
    def drink(self):
            self.thirst += 1
            return print("Thirst: " + str(self.thirst))
    
    def eat(self):
            self.hunger += 1
            return print("Hunger: " + str(self.hunger))

    
    def play(self):
            self.hunger += 1
            self.thirst += 1
            return print("Hunger: " + str(self.hunger) + ", Thirst: " + str(self.thirst))

dog = Animal()
cat = Animal()

dog.eat()
cat.play()
dog.drink()