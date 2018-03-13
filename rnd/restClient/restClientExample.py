import requests

#response = requests.get('https://api.github.com/shaiful16', auth=('user', 'password'))
response = requests.get('https://api.github.com/shaiful16')
data = response.json()

print(data)

