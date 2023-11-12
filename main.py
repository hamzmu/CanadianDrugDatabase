import requests


inp = input("Enter Drug Identification Number (DIN): ")
base = 'https://health-products.canada.ca'
url = base + '/api/drug/activeingredient/?lang=en&id=' + id
response = requests.get(url)
print(response.json())
