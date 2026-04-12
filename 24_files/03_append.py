# append to a file called john doe.txt
# it should contain data about John doe'shometown

f = open("john doe.txt", "a")

string = '''John doe initially lived in Phoenix, Arizona. He is very nice guy.'''

f.write(string)

f.close()