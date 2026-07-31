import requests

resp = requests.get("https://jsonplaceholder.typicode.com/todos/1?format=json")
print(resp.json())
