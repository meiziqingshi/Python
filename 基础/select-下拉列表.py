# coding=utf-8
# Author:jin

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://v3.bootcss.com/css/#forms")

time.sleep(15)
#driver.find_element_by_xpath("//div[@data-example-ids='select-form-control']//select[@class='form-control']").click()
'''
1.c初始化,传入select对象(直接对select进行操作,不需要要把下拉列表点出来)
2.根据下标 value属性 文本内容来选择值
'''
loc = (By.XPATH,"//div[@data-example-ids='select-form-control']//select[@class='form-control']")
WebDriverWait(driver,10).until(Ec.visibility_of_element_located(loc))
select_element = driver.find_element(*loc)

s = Select(select_element)

s.select_by_index(4)
time.sleep(3)
s.select_by_visible_text("2")
time.sleep(3)
s.select_by_index(0)
time.sleep(2)




time.sleep(5)
driver.quit()