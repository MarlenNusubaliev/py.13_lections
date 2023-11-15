from bs4 import BeautifulSoup
import requests

url = 'https://health-diet.ru/calorie'

# headers = {

# }


req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, 'lxml')
all_products = soup.find_all()
