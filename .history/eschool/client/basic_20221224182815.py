import requests

endpoint = 'http://http://localhost:8000/api//api/?abc=123'
response = requests.get(endpoint, params={'abc': 123}, json={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)