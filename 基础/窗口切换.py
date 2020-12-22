# coding = uft-8
# Author:jin

'''
1.什么情况下需要切换窗口？
2.怎么知道要切换到那个窗口？
    1）得到目前打开的所有窗口----每个窗口有一个句柄，用列表获取所有窗口的句柄：
        列表中窗口句柄的先后顺序：先出现的，先加到列表。最新的窗口，在列表的最后（-1），最先打开的窗口，在列表的最前一个（1）
        wins = driver.window_handles
    2）切换窗口
        driver.switch_to.window(wins([-1]))

    3)在新的页面里面，定位元素，操作元素
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
loc = (By.XPATH,"//a[contains(text(),' 基础教程 | 菜鸟教程')]")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_xpath("//a[contains(text(),' 基础教程 | 菜鸟教程')]").click()
time.sleep(1)
#获取当前所有窗口句柄
wins = driver.window_handles
print(wins)
#获取当前窗口句柄（就是driver.get的第一个页面，不是新点开的）
print(driver.current_window_handle)
#切换窗口
driver.switch_to.window(wins[-1])
print("切换后的窗口句柄",driver.current_window_handle)
#等待元素可见，然后点击
loc = (By.XPATH,"//img[@src='https://static.runoob.com/images/re/kkb20190819/Python3.png']")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
#*loc表示把loc拆开，取括号里面的
driver.find_element(*loc).click()
wins = driver.window_handles
print(wins)




time.sleep(5)
driver.quit()
