import requests

endpoint = 'http://127.0.0.1:8000/api/?abc='
response = requests.get(endpoint, params={'abc': 123}, data={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)