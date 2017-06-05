import requests,bs4
import re
import webbrowser
url='http://www.amazon.in/Smartphones-Under-%E2%82%B910-000-Basic-Mobiles/s?ie=UTF8&page=1&rh=n%3A1805560031%2Cp_36%3A-1000000'
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,"html.parser")
collect= soup.select('.s-access-detail-page')
count=0;
for elems in collect:
    if count>10:
        break
    str=elems.get('href')
    count=count+1
    webbrowser.open(str)









