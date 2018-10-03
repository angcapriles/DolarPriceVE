# Import  Libraries
import urllib2
import notify2 
from bs4 import BeautifulSoup


def fetchDolarPriceMonitor():
    # Specify the URL

    quote_page = 'https://twitter.com/MonitorDolarVe'

    # Query the website and return the html to the variable 'page'

    page = urllib2.urlopen(quote_page)

    # Parse the html using beautiful soup  and store in variable 'soup'

    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div>  of name and get its value

    name_box = soup.findAll('p', attrs={'class':'tweet-text'})

    #name = name_box.text.strip() # strip() is used to remove starting
    lista = []
    for node in name_box:
        for line in node:
            if 'Promedio general' in line:
                lista.append(line[20:-49])

    return lista[0]

def fetchDolarPriceDtoday():
    url = urllib2.urlopen("https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate.js")
    content = url.readlines()
    valorDolar = content[44].replace('"dolartoday": ', '')
    return valorDolar.replace('  ', '')

