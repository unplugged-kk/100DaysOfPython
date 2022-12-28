import requests
import bs4
product_url = "https://www.kishorekumar.today"

res = requests.get(product_url, timeout=5)
# print(res.status_code)
# print(res.text)
if res.status_code != 200:
    pass

soup = bs4.BeautifulSoup(res.text, "html.parser")
