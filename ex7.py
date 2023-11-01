import requests
payload = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"


print("Without params method\n\n")

response = requests.get(url=url)
print("Method: get\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:", response.status_code,
"\nResponse headers:", response.headers, "\n\n")


print("\n\n\nWrong method\n\n")
response = requests.head(url=url)
print("Method: head\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:", response.status_code,
"\nResponse headers:", response.headers, "\n\n")



print("\n\n\nRight method\n\n")
response = requests.request(url=url, method="GET")
print("Method GET:", "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
      response.status_code, "\nResponse headers:", response.headers, "\n\n")


print("\n\n\nAll combinations\n\n")

for check_method in payload:
    response = requests.get(url=url, params=check_method)
    print("For method GET:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")

    response = requests.post(url=url, data=check_method)
    print("For method POST:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")
    response = requests.head(url=url, data=check_method)

    response = requests.put(url=url, data=check_method)
    print("For method PUT:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")

    response = requests.delete(url=url, data=check_method)
    print("For method DELETE:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")

    response = requests.head(url=url, data=check_method)
    print("For method HEAD:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")

    response = requests.options(url=url, data=check_method)
    print("For method OPTIONS:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")

    response = requests.patch(url=url, data=check_method)
    print("For method PATCH:", check_method, "\nResponse:", response, "\nResponse text:", response.text, "\nStatus code:",
          response.status_code, "\nResponse headers:", response.headers, "\nResponse request", response.request, "\n\n")
