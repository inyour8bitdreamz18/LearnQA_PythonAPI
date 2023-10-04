print("Hello world from Anna P.")
import requests
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)