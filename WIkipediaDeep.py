# Opens a wikipedia page and parses it to 3 levels deep
# List the URLs at each level
# Top 5 links only
from selenium import webdriver

import bs4,requests
import re
links=[]
def scrapetop5links(url):
    count=0
    res = requests.get(url)
    pos=re.search('From Wikipedia',res.text).start()
    soup = bs4.BeautifulSoup(res.text[pos:], 'html.parser')
    global links
    links = soup.select('a')
    for indlink in links:
        count=count+1
        if count<=5:
            print('https://en.wikipedia.org' + str(indlink.get('href')))

def fxn():
    scrapetop5links('https://en.wikipedia.org' + str(links[0].get('href')))
    scrapetop5links('https://en.wikipedia.org' + str(links[1].get('href')))
    scrapetop5links('https://en.wikipedia.org' + str(links[2].get('href')))
    scrapetop5links('https://en.wikipedia.org' + str(links[3].get('href')))
    scrapetop5links('https://en.wikipedia.org' + str(links[4].get('href')))




url='https://en.wikipedia.org/wiki/ARPANET'
scrapetop5links(url)
fxn()





