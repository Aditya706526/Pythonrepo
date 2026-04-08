class employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"

    def __repr__(self):
        return f"name: {self.name} \nsalary: {self.salary}"
    
e = employee("Adi", 3400)
print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e.name))