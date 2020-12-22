# coding = uft-8
# Author:jin

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#引入隐性等待模块
from selenium.webdriver.support.wait import WebDriverWait
# 简称EC模块 主要有显性等待、判断title等方法

from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
#隐性等待
driver.implicitly_wait(10)
#get方法，页面会完全加载完才会执行下面的
driver.get("https://www.taobao.com")
time.sleep(3)
# driver.find_element_by_id("q").send_keys("印花卫裤女")
# driver.find_element_by_class_name("search-button").click()
# time.sleep(3)
driver.find_element_by_xpath("//a[text()='手表']").click()
time.sleep(10)
driver.close()

#定位策略
loc = (By.XPATH,"//a[text()='手表']")
#EC.visibility_of_element_located(loc)
'''
前面设置等待条件 10代表等待10秒 后面还要轮询周期 
  （driver，15，0.5）默认等待上限为15秒 默认轮询周期是0.5秒（多少秒去确认一下条件是否成立）
直到loc元素可见

页面元素出现新的操作后，需要等待

'''
#如果等待10秒，这个元素还没有出现，就会抛出异常
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))

driver.find_element(By.XPATH,"//a[text()='手表']")


#//span[@class='lead-fontSize' and contains (text(),'服务事件')]
#//div[@class='el-menu--horizontal']
#//input[@placeholder="请输入用户名称"]


