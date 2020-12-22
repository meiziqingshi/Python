# coding = utf-8
# Author:jin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

pha_js = "var a = arguments[0]; a.readOnly = false; a.value = \"2021-08-08\";"#js语句，修改属性readOnly = false 可写，value传入日期值

loc = ("id","train_date")
ele = driver.find_element(*loc)
time.sleep(5)

driver.execute_script(pha_js, ele)
time.sleep(5)
#第二种传入日期---可变的
now_date = "2020-12-31"
pha_js = "var a = arguments[0]; a.readOnly = false; a.value = arguments[1];"
driver.execute_script(pha_js, ele, now_date)
time.sleep(5)


#第三种 当输入框使用的是选择控件且为只读状态时，selenium 原生 API 无法操作控件，可以通过 js 移除
String_js = "document.getElementById('train_date').removeAttribute('readonly')"#去除属性
driver.execute_script(String_js)
time.sleep(5)
# driver.find_element(By.ID("train_date")).send_keys(Keys.CONTROL,"a")#清空
# time.sleep(5)
# driver.find_element(By.ID("train_date")).send_keys(Keys.BACK_SPACE)#清空
# driver.find_element(By.ID("train_date")).send_keys("2021-03-30")#输入

driver.find_element_by_id('train_date').clear()#清空
driver.find_element_by_id('train_date').send_keys("2021-03-30")#输入


#******************************************Js语句练习**************************************

String_js = "var a = document.getElementById('fromStationText'); a.value = '成都';"
loc = ("id","fromStationText")
ele = driver.find_element(*loc)
time.sleep(5)
driver.execute_script(String_js,ele)
time.sleep(5)

String_js = "document.getElementById('fromStationText').value = '北京'"
driver.execute_script(String_js)




time.sleep(5)
driver.quit()


'''
在对元素进行操作的时候，注意元素的变化，如它的value，在选择值后，value就会改变
但是自动化的时候，对这个元素进行鼠标操作的时候，它的value值并没有改变，所以会导致自动化脚本报错
该情况下就需要写js语句来传入这个元素的value值
还有一种复杂的输入框：textarea 文本域 ，在element页看不见对它的写入值，需要在console里面用js操作才能看见写入的值
    该情况下也不能再自动化脚本对直接对这个元素进行鼠标操作，需要在自动化脚本中用js语句来进行赋值
'''
