# coding = uft-8
# # Author:jin

from selenium import webdriver
import time

driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("http://www.imooc.com")
time.sleep(3)
driver.find_element_by_id("js-signin-btn").click()
#driver.find_element_by_id("js-signin-btn") --叫做WbElement对象 可以继续寻找元素
time.sleep(3)
driver.find_element_by_name("email").send_keys("15184337818@163.com")
driver.find_element_by_name("password").send_keys("w900370.")
driver.find_element_by_class_name("moco-btn").click()
time.sleep(5)
driver.get("https://www.imooc.com/user/setbindsns")
driver.find_elements_by_class_name("inner-i-box")[1].find_element_by_class_name("moco-btn-normal").click()
time.sleep(10)

#用列表获取当前所有页面窗口的id?
hand_list = driver.window_handles
#获取当前页面id
current_handle = driver.current_window_handle
print(hand_list)
for handle in hand_list:
    '''
    判断是否当前页面
    适用于两个页面窗口
    '''
    print(handle)
    print(current_handle)
    time.sleep(5)
    if handle != current_handle:
        driver.switch_to.window(handle)
        print("句柄切换成功")
        driver.find_element_by_id("jump_login_url_a").click()
        driver.find_element_by_id("username").send_keys("test")
        time.sleep(10)

driver.close()

