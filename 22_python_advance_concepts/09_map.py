num = [1, 2, 3, 4, 5, 67, 8, 9, 545]

def sqare(x):
    return x * x

new = map(lambda x: x * x, num)
print(list(new))