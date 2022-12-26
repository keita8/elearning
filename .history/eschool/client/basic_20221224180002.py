import requests

endpoint = 'http://httpbin.org'
response = requests.get(endpoint, json={'Salutation':'Bonjour'})

print(response.text)