import requests,bs4
import re
import webbrowser
url='http://www.amazon.in/Moto-Play-4th-Gen-Black/dp/B01FM7GIR4/ref=sr_1_1?ie=UTF8&qid=1494628075&sr=8-1&keywords=moto+e3+power'
res=requests.get(url)
print(res.text)
soup=bs4.BeautifulSoup(res.text,"html.parser")
collect= soup.select('.a-link-normal')
count=0
for elems in collect:
    print(elems)









