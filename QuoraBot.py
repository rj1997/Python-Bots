import os
os.environ["HTTPS_PROXY"] = "http://ipg_2015003:abhi%4098@192.168.1.107:3128"
from selenium import webdriver
path="C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser=webdriver.Chrome(path)
url='https://www.quora.com/Why-is-Facebook-successful'
browser.get(url)

