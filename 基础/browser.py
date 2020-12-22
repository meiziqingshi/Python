# coding = utf-8
# Author:jin

from selenium import webdriver
import time
from selenium.webdriver.support import  expected_conditions as EC

class SeleniumDriver(object):
    #获取driver的值
    def __init__(self,browser):
        self.driver = self.open_browser(browser)

    def open_browser(slef,browser):
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Firefox":
            driver = webdriver.firefox()
        else:
            driver = webdriver.Edge()
        driver.maximize_window()
        #driver.minimize_window()
        time.sleep(5)
        return driver

    def get_url(self,url):
        self.driver.get(url)

    def assert_title(self,title_name = None):
        '''
        判断title是否正确
        '''
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def switch_window(self,title_name = None):
        '''
        切换窗口
        '''
        handle_list = self.driver.window_handles #获取所有页面窗口id
        current_handle = self.driver.current_window_handle #获取当前页面窗口id
        print(handle_list)
        print(current_handle)
        for handle in handle_list:
            if handle != current_handle:
                time.sleep(2)
                self.driver.switch_to.window(handle) #切换窗口
                if self.assert_title(title_name):
                    '''
                    判断是否为传入的页面
                    是传入页面，就终止循环
                    '''
                    break
        time.sleep(10)
        driver.find_element_by_id("jump_login_url_a").click()
        driver.find_element_by_id("username").send_keys("test")
        time.sleep(10)

    def close_browser(self):
        self.driver.close()

#driver = open_browser("Chrome")
driver = SeleniumDriver("Chrome")
driver.get_url("http://www.imooc.com")
#time.sleep(10)
#print(driver.assert_title("慕课网"))
time.sleep(100)
driver.switch_window("网站连接")
time.sleep(5)
#关闭当前窗口
driver.close_browser()
#退出会话-关闭浏览器，关闭chromedriver这个进程
driver.quit()

'''
前进、后退、刷新(有多窗口的历史纪录)
'''

driver.back()
driver.forward()
driver.refresh()
