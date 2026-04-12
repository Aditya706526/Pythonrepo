# Write to a file called John Doe.txt
# It should contain data about John Doe

f = open("john doe.txt", "w")

string = '''Jon doe is a nice guy and he work with python and his favorite package in python is pandas.
'''

f.write(string)

f.close()