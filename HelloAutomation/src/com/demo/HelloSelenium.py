# coding=utf-8
from selenium import webdriver

from com.demo import content
from time import sleep, clock


print("your input is :%r" %content)
print(clock())
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click
sleep(5)
driver.quit()