coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

corlist = list(coordinates)
corlist[0] = 50

coordinates = tuple(corlist)

print(coordinates, type(coordinates))