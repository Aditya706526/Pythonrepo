
def divide(a,b):
    try:
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None

    finally:
        print("always executed")


a = int(input("Enter 1st number:\n"))
b = int(input("Enter 2nd number:\n"))
divide(2,3)