import requests
from bs4 import BeautifulSoup
import locale
import numpy as np

locale.setlocale(locale.LC_NUMERIC,"pl")
link = ("https://www.otomoto.pl/osobowe/bmw"
       "?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_registered%5D="
        "1&search%5Bfilter_enum_no_accident%5D=1&search%5Border%5D=filter_float_price"
        "%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=")


priceSum = []

def parseLink(link):
    global priceSum
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all(class_="offer-price__number ds-price-number")
    for price in prices:
        intPrice = locale.atof(price.span.string.replace(' ',''))
        print(intPrice)
        priceSum.append(intPrice)
    return soup

def removeOutliers(priceSum):
    an_array = np.array(priceSum)
    mean = np.mean(an_array)
    standard_deviation = np.std(an_array)
    distance_from_mean = abs(an_array - mean)
    max_deviations = 2
    not_outlier = distance_from_mean < max_deviations * standard_deviation
    return an_array[not_outlier]


count = 1
soup = parseLink(link)
while len(soup.find_all(class_="next abs")) > 0:
    count += 1
    soup = parseLink(link + "&page=" + str(count))
    print(count)
    
no_outliers = removeOutliers(priceSum)
print(np.sum(no_outliers)/len(no_outliers))