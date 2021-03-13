import time
from selenium import webdriver



driver = webdriver.Chrome()
driver.get('https://www.nike.com/')
searchbox = driver.find_element_by_xpath(' //*[@id="gen-nav-commerce-header-v2"]/div[3]/header/div/div[1]/div[2]/nav/div[2]/ul/li[2]/a')
searchbox.click()
time.sleep(5)

searchbox = driver.find_element_by_xpath('//*[@id="dd5f142c-8973-47e1-8ebf-d7a95ed22a3a"]/div/div/div/div/div/div[1]/ul/li[1]/a')
searchbox.click()
//*[@id="wallNavFG2"]/a/div
time.sleep(5)
searchbox = driver.find_element_by_xpath('//*[@id="wallNavFG3"]/a[1]/div')
searchbox.click()

time.sleep(5)
searchbox = driver.find_element_by_xpath('//*[@id="wallNavFG3"]/a[8]/div')
searchbox.click()

time.sleep(5)
searchbox = driver.find_element_by_xpath('//*[@id="wallNavFG3"]/a[7]/div')
searchbox.click()

