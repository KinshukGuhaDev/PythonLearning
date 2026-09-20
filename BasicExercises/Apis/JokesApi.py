import requests
response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
jokes = response.json()
for joke in jokes:
    print(f"{joke['setup']} - {joke['punchline']}")