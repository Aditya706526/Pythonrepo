f = open("adi.txt", "r")

for line in f:
    print(line)
content = f.read()

f.close()