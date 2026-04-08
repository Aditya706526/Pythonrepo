s = {3, 23, 2, 11}
print(s, type(s))
# print(s[3]) elemets cannot be located using index as sets are unordered

s.add(32)
print(s)
s.add(33)
s.remove(2)
print(s)