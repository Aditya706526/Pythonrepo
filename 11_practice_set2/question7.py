num = int(input("Enter a number: \n"))
for i in range(1, 11):
    print(str(num) + "x" + str(i) + "=" + str(num * i))

sum = 0
for i in range(1, 101):
    # print(i)
    sum += i
print("sum of 1 - 100 is: ", sum)