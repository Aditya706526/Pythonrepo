num = int(input("Enter a number between 1 - 7:\n"))
if(num > 0 and num <= 7):
    match num:
        case 1: print("Monday")
        case 2: print("Tuesday")
        case 3: print("Wednesday")
        case 4: print("Thursday")
        case 5: print("Friday")
        case 6: print("Saturday")
        case 7: print("Sunday")
else:
    print("Invalid input")

