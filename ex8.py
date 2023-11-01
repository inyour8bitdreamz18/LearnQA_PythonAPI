import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response1 = requests.get(url=url)
req_text = response1.json()
token = req_text["token"]
t_left = int(req_text["seconds"])

response2 = requests.get(url=url, params={"token": token})
req_text = response2.json()

if req_text["status"] == "Job is NOT ready":
    time.sleep(t_left+1)
    response3 = requests.get(url=url, params={"token": token})
    print(response3.text)
    req_text = response3.json()
    if req_text["status"] == "Job is ready" and "result" in req_text:
        print("SUCCESS")
else:
    print("Something wrong")