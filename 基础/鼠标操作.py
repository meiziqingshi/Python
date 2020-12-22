# coding = utf-8
# Author:jin

'''
鼠标操作:(ActionChains类)
    悬浮.move_to_element
    点击.click
    双击.double_click
    右键.context_click
    拖拽.drag_and_drop
    暂停.pause

    1.将所有的鼠标的动作,先放到一个列表中
    2.perform():执行鼠标动作
'''

from selenium import webdriver
#action_chains类常用于模拟鼠标的行为
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#driver.find_element_by_id("s-usersetting-top").click()
'''
1)找到鼠标元素
2)实例化ActionChains类
3)调用鼠标行为:悬浮---(move_to_element返回的也是一个实例化) 储存鼠标行为
    悬浮然后点击----ac.move_to_element(ele).click(ele)
4)调用perform()来执行鼠标动作 perform()这个函数作业----执行所有存储的动作。

'''
loc = (By.ID,"s-usersetting-top")
ele = driver.find_element(*loc)
print(ele)
ac = ActionChains(driver)
ac.move_to_element(ele)
ac.perform()

#ActionChains(driver).move_to_element(ele).perform()

# time.sleep(2)
# driver.find_element(By.XPATH,"//a[text()='高级搜索']").click()

loc = (By.XPATH,"//a[text()='高级搜索']")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


#***************************************Select类*********************
from selenium.webdriver.support.select import Select



time.sleep(5)
#driver.quit()
