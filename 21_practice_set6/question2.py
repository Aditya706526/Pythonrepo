class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"The name of the person is {self.name} and age is {self.age}")


a = person("Adi", 25)
a.info()