import requests,bs4
import re
import webbrowser
inpstring=input('Enter your query : ')
inpstring.replace(' ','+')
url='https://www.google.com/search?q='+inpstring
res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,"html.parser")
collect= soup.select('.r a')
count=0
for elems in collect:
    str=elems.get('href')
    #print(str)
    flag=re.search('http://(.+?)&sa',str)
    if count > 5:
        break
    if flag:
        found=flag.group(1)
        finalstr='http://'+found
        webbrowser.open(finalstr)
        count=count+1
print('Total pages opened : %s'%count)








