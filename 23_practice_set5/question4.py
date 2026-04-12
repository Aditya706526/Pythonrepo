class MathUtils:
    def __init__(self):
        pass 
        
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def description(cls):
        print("This is a utility class for the math operations.")

a = MathUtils
print(a.add(3, 5))
a.description