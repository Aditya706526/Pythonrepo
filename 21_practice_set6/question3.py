class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("some sound")

class dog(Animal):
    def sound(self):
        super().sound()
        print("Bark !")

d = dog("Pluto")
d.sound()