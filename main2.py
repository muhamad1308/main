import requests

url = "https://randomuser.me/api/"
qwer = {'results':3,'gender':'male','nat':'us'}
r = requests.get(url,qwer)
j = r.json()['results']

#print(r.url)
print(r.status_code)
print(r.url)
