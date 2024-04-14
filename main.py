import requests

url = 'https://randomuser.me/api/'

r = {'resulsts':1}

re=requests.get(url,r)
#print(re.json())
print(re.url)