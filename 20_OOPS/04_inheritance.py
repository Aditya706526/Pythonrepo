class animal: # parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Generic animal sound")

class dog(animal):
    def speak(self):
        super().speak() # we are using the speak function of parent class
        print("woof !!!")



# a = animal("Dog")
# a.speak()

d = dog("Pluto")
d.speak()
print(d.location)
