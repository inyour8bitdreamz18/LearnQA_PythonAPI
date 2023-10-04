import requests

print("Hello world from Anna P.")

'''From presentation
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)'''

#for 4th task
response = requests.get('https://playground.learnqa.ru/api/get_text')
print("Results:", response.text)