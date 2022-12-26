import requests

endpoint = 'http://:8000/api/?abc=123'
response = requests.get(endpoint, params={'abc': 123}, json={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)