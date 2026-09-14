import requests

data = requests.get('https://ipinfo.io').json()

# print(data)

print(data["loc"])
# print(f"City: {data.get('city', 'N/A')}")
# print(f"Region: {data.get('region', 'N/A')}")
# print(f"Country: {data.get('country', 'N/A')}")   



new_data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=25.32&longitude=82.98&current=temperature_2m").json()

# print(new_data["current"]["time"])
# print(new_data["current"]["temperature_2m"])
# print(new_data)
