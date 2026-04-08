txt = "Hi my name is Aditya Sharma and I am a data engineer"
vowels = ['a','e','i','o','u']
sum = 0
for char in txt.lower():
    if(char in vowels):
        sum += 1
print(f"there are {sum} no. of vowels in string")
