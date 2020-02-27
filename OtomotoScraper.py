import requests
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_NUMERIC,"pl")
link = ("https://www.otomoto.pl/osobowe/opel/mokka/"
       "?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_registered%5D="
        "1&search%5Bfilter_enum_no_accident%5D=1&search%5Border%5D=filter_float_price"
        "%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=")

def execute(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all(class_="offer-price__number ds-price-number")
    for price in prices:
        intPrice = locale.atof(price.span.string.replace(' ',''))
        print(intPrice)
    return soup


count = 1
soup = execute(link)
while len(soup.find_all(class_="next abs")) > 0:
    count += 1
    soup = execute(link + "&page=" + str(count))
    print(count)