from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromepath="C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser=webdriver.Chrome(chromepath)
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
email='rishabhrjjain1997@gmail.com'
receipt='rishabhjaingennius@gmail.com'
password='8'
adi=browser.find_element_by_xpath('//*[@id="identifierId"]')
adi.send_keys(email)
adi.send_keys(Keys.RETURN)
import time
time.sleep(2)
adi=browser.find_element_by_name('password')
adi.send_keys(password)
adi.send_keys(Keys.RETURN)
time.sleep(10)
adi=browser.find_element_by_xpath('//*[@id=":io"]/div/div')
time.sleep(1)
adi.click()
time.sleep(1)
adi=browser.find_element_by_xpath('//*[@id=":o2"]')
adi.click()
time.sleep(1)
adi.send_keys(receipt)
adi.find_element_by_xpath('//*[@id=":nh"]')
time.sleep(1)
adi.click()
time.sleep(1)
adi.send_keys('Sent using Python ')
time.sleep(1)
adi.send_keys(Keys.TAB)
time.sleep(1)
adi.send_keys("Manma")
time.sleep(1)
browser.find_element_by_xpath('//*[@id=":md"]').click()










