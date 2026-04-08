import requests

git = requests.get("https://api.github.com")

print(git.json())