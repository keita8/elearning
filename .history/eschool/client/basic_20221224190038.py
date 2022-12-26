import requests

endpoint = 'http://localhost:8000/api/?params'
response = requests.get(endpoint, params={'abc': 123}, json={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)