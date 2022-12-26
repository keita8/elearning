import requests

endpoint = 'http://localhost:8000/account/teacher/'
response = requests.get(endpoint)

print(response.text)
print(response.status_code)