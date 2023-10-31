import requests
from json.decoder import JSONDecodeError
'''
print("Hello world from Anna P.")

#From presentation
payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)

#for 4th task

response = requests.get("https://playground.learnqa.ru/api/get_text")
print("Results:", response.text)

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")

#Only get-request has params, post etc - data!

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)


response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.text)

# 100-199 - info
# 200-299 - success
# 300-399 - redirect
# 400-499 - client's error
# 500-599 - server error

reqs = ["https://playground.learnqa.ru/api/get_500", "https://playground.learnqa.ru/api/smth"]
for r in reqs:
    response = requests.post(r)
    print(response.status_code)
    print(response.text)


responseF = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print('\nForbidden redirection:', responseF.status_code)
print(responseF.text)

responseT = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print('\nAllowed redirection:', responseT.status_code)
print(responseT.text)
#get the first response in the massive
first_response = responseT.history[0]
#default the last url (last response)
second_response = responseT

print(first_response.url)
print(second_response.url)


headers = {"some_headers": "123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print("Data that we SENT to server:", response.text)
print("Data that we RECEIVED from server:", response.headers)

payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print("Text:", response.text)
print("Status:", response.status_code)
print("Cookies:", dict(response.cookies))
print(response.headers)
'''

payload = {"login": "secret_login", "password": "secret_pass222"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get("auth_cookie")

cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)
