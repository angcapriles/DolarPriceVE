from bs4 import BeautifulSoup
import requests
import urllib2 
url = urllib2.urlopen("https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate.js")
content = url.readlines()
valorDolar = content[44].replace('"dolartoday": ', '')
print valorDolar

