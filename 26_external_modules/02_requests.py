import requests
r = requests.get('https://api.github.com/users/Aditya706526')
with open("codewithadi.txt", "w") as f:
    f.write(r.text)