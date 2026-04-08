print("Hello Adi")
print(3)

with open("adi.txt", "w") as file:
    file.write("Hello")
    file.write("\nNew file")
print("file created and written succefully")

with open("adi1.txt", "r") as file:
    content = file.read()
    print(content)

with open("adi2.txt", "w") as file:
    file.write("Hello")
print("written successfully")


