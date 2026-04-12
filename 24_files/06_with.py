# f = open("adi.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("adi.txt", "r") as f:
    content = f.read()
    print(content)
    # no need to write f.close() as file is closed be default
    