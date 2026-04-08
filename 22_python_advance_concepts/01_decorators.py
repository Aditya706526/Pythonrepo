def decorator(func):
    def wrapper():
        print("About to execute a function")
        func()
        print("Executed the function")
    return wrapper
@decorator
def say_hello():
    print("Hello !")

say_hello()
# f = decorator(say_hello)
# f()