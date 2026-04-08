try:
    a = 345/0
except Exception as e:
    print(e)

# Gets executed when there is no errors in the try block.
else:
    print("hey I'm good")