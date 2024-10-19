import requests

url = 'http://127.0.0.1:5001/chat'

# Question: What is the release year of The Lion King?
data = {'message': 'What is the release year of The Lion King?'}
response = requests.post(url, json=data)
print(response.json())

# Question: What is the release year of Mulan?
data = {'message': 'What is the release year of Mulan?'}
response = requests.post(url, json=data)
print(response.json())

# Question: What is the release year of The Mulan 2?
data = {'message': 'What is the release year of The Mulan 2?'}
response = requests.post(url, json=data)
print(response.json())

# Question: What is the release year of Aladdin 1, 2 and 3?
data = {'message': 'What is the release year of Aladdin 1, 2 and 3?'}
response = requests.post(url, json=data)
print(response.json())

# Question: What year was Walt Disney Company founded?
data = {'message': 'When was Disney founded?'}
response = requests.post(url, json=data)
print(response.json())

# Question: Who founded Walt Disney Company?
data = {'message': 'Who founded Walt Disney Company?'}
response = requests.post(url, json=data)
print(response.json())

# Question: Who is the current CEO of Walt Disney Company?
data = {'message': 'Current CEO of Walt Disney Company?'}
response = requests.post(url, json=data)
print(response.json())
