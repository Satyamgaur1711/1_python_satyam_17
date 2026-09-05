import requests

api_url = "https://official-joke-api.appspot.com/random_joke"

print("your new joke are loading...")

response = requests.get(api_url)

deta = response.json()

print("ye raha tumhara joke")

# print(deta)

# hear deta ek dictionary hai jisme 4 key value pair hai  first type, second setup, third punchline, fourth id.
jock_setup = deta["setup"]

jock_punchline = deta["punchline"]

print("jock setup: ", jock_setup)
print("jock punchline: ", jock_punchline)

# we only extract the setup and punchline from the dictionary and print them separately.




