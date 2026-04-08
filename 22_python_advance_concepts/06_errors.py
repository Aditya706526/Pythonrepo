# while True:
#     try:
#         a = int(input("Enter 1st number:\n"))
#         b = int(input("Enter 2nd number:\n"))
#         print(f"division is : {a / b}")

#     except ValueError:
#         print("bad calculation")

#     except ZeroDivisionError:
#         print("zero is exception")
#     except Exception as e:
#         print("Some error occured:", e)

a = int(input("Enter 1st number:\n"))
b = int(input("Enter 2nd number:\n"))
if b == 0:
    raise ValueError("don't devide by zero")
print(f"division is : {a / b}")