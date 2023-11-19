import requests
#python -m pytest -s training/ex11.py

class TestCheckCookieName:
    def test_check_cookie_name(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url=url)
        cookies = dict(response.cookies)
        print(cookies)
        cookie_name = tuple(cookies.keys())[0]
        expected_name = "HomeWork"

        assert cookie_name == expected_name
