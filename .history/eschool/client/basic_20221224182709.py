import requests

endpoint = 'http://127.0.0.1:8000/api/?p'
response = requests.get(endpoint, params={'parametres': 123}, data={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)