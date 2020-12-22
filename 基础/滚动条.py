# coding = utf-8
# Author:jin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

driver = webdriver.Chrome()
driver.get("https://v3.bootcss.com/css/#forms")

loc = (By.XPATH,"//div[@data-example-ids='select-form-control']//select[@class='form-control']")
WebDriverWait(driver,10).until(Ec.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
'''
上面可以看出这个页面是自己滚动的
'''
time.sleep(5)
#滚动到页面顶端 默认为顶端--- True
driver.execute_script("arguments[0].scrollIntoView();",ele) #arguments接受外部参数 列表

time.sleep(5)

#滚动到页面底部
driver.execute_script("arguments[0].scrollIntoView(False);",ele)

time.sleep(5)

#滚动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(5)

#滚动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

time.sleep(5)
driver.close()
