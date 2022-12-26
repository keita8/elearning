import requests

endpoint = "http://localhost:8000/account/all-users/"
response = requests.get(endpoint)

print(response.text)
print(response.status_code)
