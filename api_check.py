import requests

api_key = "32d00dc9835516c2c908e62f"
url = f"https://v6.exchangerate-api.com/v6/32d00dc9835516c2c908e62f/latest/INR"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Conversion rates:", data['conversion_rates'])
else:
    print("Failed to fetch data:", response.status_code, response.text)
