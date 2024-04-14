import requests

url = 'https://randomuser.me/api/?results=3&gender=male&nat='

r = requests.get(url)
data = r.json()['results']
for i in data:
    print(i['name'],i['nat'])
