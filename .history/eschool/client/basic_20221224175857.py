import requests

endpoint = 'http://httpbin.org'
response = requests.get(endpoint, json={''})

print(response.text)