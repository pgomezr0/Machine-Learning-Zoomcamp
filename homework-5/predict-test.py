#!/usr/bin/env python
# coding: utf-8

import requests

url = "http://localhost:8000/predict"


client = {"job": "student", "duration": 280, "poutcome": "failure"}


requests.post(url, json=client)
response = requests.post(url, json=client).json()
print(response)

