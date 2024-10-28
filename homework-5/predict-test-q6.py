import requests

url = "http://localhost:8000/predict"


client = {"job": "management", "duration": 400, "poutcome": "success"}

requests.post(url, json=client)
response = requests.post(url, json=client).json()
print(response)

