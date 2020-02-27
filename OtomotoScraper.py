import requests
page = requests.get("https://www.otomoto.pl/osobowe/opel/mokka/")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
prices = soup.find_all(class_="offer-price__number ds-price-number")
for price in prices:
    intPrice = int(price.span.string.replace(' ',''))
    print(intPrice)