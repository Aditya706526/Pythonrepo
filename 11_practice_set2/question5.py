num1 = int(input("Enter 1st digit\n"))
num2 = int(input("Enter 2nd digit\n"))
op = input("Enter operator\n")
match op:
    case '+': print("sum is: ", num1 + num2)
    case '-': print("difference is: ", num1 - num2)
    case '*': print("product is: ", num1 * num2)
    case '/': print("division is: ", num1 / num2)