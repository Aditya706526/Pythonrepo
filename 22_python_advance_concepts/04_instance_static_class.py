class employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # this is an instance method (default)
    def print_info(self):
        info =  f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a, b):
        return a + b
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        

e1 = employee("Jack", 3455)
e2 = employee("Jill", 3455)
print(employee.company)
# print(employee.name) # this will throw an error
e1.print_info()
e2.print_info()

print(e2.sum(5,23))

e1.print_company()
e1.change_company("Acer")
print(employee.company)