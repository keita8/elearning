import requests

endpoint = 'http://httpbin.org'
response = requests.get(endpoint, params={'param'} data={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)