class employee:
    company = "Asus" # Class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
        
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}. The bond is for {self.bond} years")

    
e1 = employee(34000, "John", 4, "Tesla")
print(e1.company) # will always print instance attribute if present but if not present then class attribute will be printed.
print(employee.company) # will always print class attribute
# object introspection (it's a way to check all the methods within a class)

print(dir(e1))
