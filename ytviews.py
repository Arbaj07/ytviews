from selenium import webdriver
import time
views = int(input("enter no. of view:1000"))
view_time = float(input('enter time for each view:5'))

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser3 = webdriver.Chrome()

# put video link in 'https://www.youtube.com/watch?v=2j7fD92g-gE&t=332s'
for i in range(1000):
    browser1.get('')
    time.sleep(5)
    browser2.get('')
    time.sleep(1)
    browser3.get('')
    time.sleep(1)

browser1.close()
browser2.close()
browser3.close()
# script by abhishek5999
