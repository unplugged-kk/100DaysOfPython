import requests

x = requests.get('https://httpbin.org/get')
print(x.text)
