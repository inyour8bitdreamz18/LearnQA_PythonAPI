import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
all_response = response.history
print(all_response)
print(response.url)
print(len(all_response))
