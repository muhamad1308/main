import requests

url = 'https://randomuser.me/api/'

r = {'results':2}

re=requests.get(url,r)
print(re.json())
