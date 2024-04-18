import requests

url = "https://randomuser.me/api/"
qwer = {
    'results':3,
    'gender':'male',
    'nat':''
    }
r = requests.get(url,qwer)
j = r.json()['results']

print(r.status_code)
print(r.url)
for i in j:
    print(i['name'],i['nat'])
