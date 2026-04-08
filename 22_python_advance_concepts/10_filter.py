def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
a = [1, 2, 4532, 65, 432, 65, 45, 35, 5, 3, 6, 8, 5, 4, 2]

new = filter(lambda x: x > 9, a)

print(list(new))