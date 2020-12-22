# coding = uft-8
# Author:jin

'''
1.识别元素是否在iframe中
2.切换
    1）切换到哪个iframe
        iframe是标签对，是当前默认HTML的一个元素。  //iframe[@标签名='']
        支持3种方式来切换到哪个iframe：
            iframe下标-------------driver.switch_to.frame() 从0开始
            iframe元素的name属性----driver.switch_to.frame("name值")
            iframe这个webElment----driver.switch_to.frame(driver.find_element_by_xpath(路径值))
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ke.qq.com/")
# print(driver.current_window_handle)
driver.find_element_by_id("js_login").click()
loc = (By.XPATH, "//a[text()='QQ登录']")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# print(driver.current_window_handle)
time.sleep(10)
#切换到iframe框
driver.switch_to.frame("login_frame_qq")
# print(driver.current_window_handle)
loc = (By.ID, "switcher_plogin")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(* loc).click()
loc = (By.ID,'u')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("112111")
time.sleep(10)
#回到上一级的iframe--上一代
driver.switch_to.parent_frame()
loc = (By.ID, "login_close")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
time.sleep(5)
driver.find_element_by_id("js_login").click()


# #回到默认的html页面--第一代
# driver.switch_to.default_content()
# #回到上一级的iframe--上一代
# driver.switch_to.parent_frame()


time.sleep(10)
driver.quit()

'''
切换iframe窗口的时候 强制等待10秒
'''