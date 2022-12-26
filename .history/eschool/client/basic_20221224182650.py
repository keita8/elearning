import requests

endpoint = 'http://12'
response = requests.get(endpoint, params={'parametres': 123}, data={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)