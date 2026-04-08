# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7  8  9

# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(0) + fib(1)
# fib(3) = fib(1) + fib(2)
# fib(n) = fib(n-2) + fib(n-1)

def fib(n):
    if(n == 0 or n == 1):
        return n

    return fib(n-2) + fib(n-1)

print(fib(6))

fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(3) + fib(4)
fib(0) + fib(1) + fib(1) + fib(2) + fib(1) + fib(2) + fib(2) + fib(3)
0 + 1 + 1 + fib(0) + fib(1) + 1 + fib(0) + fib(1) + fib(0) + fib(1) + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1