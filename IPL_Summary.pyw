#IPL UPDATE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromepath="C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser=webdriver.Chrome(chromepath)
browser.get('http://www.iplt20.com/')
import time
time.sleep(5)
for i in range(1,1000):
    obj = browser.find_element_by_class_name('summary')
    print(obj.text)
    time.sleep(10)

