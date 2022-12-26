import requests

endpoint = 'http://httpbin.org'
response = requests.get(endpoint, ={'Salutation':'Bonjour'})

print(response.text)
print(response.status_code)