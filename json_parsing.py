import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)
print(obj['answer'])

key = ["answer", "answer2"]
for k in key:
    if k in obj:
        print(obj[k])
    else:
        print(f"Ключа {k} в JSON нет")