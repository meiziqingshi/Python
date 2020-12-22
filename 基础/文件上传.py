# coding = utf-8
# Author:jin

from selenium import webdriver
import pywinauto
from pywinauto.keyboard import send_keys
import time

url= "https://www.layui.com/demo/upload.html"
browser = webdriver.Chrome()
# 访问图片上传的网页地址
browser.get(url=url)
# 点击图片上传按钮，打开文件选择窗口
browser.find_element_by_xpath("//button[@id='test2']").click()

time.sleep(5)

'''
# 使用pywinautoc创建一个操作桌面窗口的对象
app = pywinauto.Desktop()
# 选中文件上传的窗口
dlg = app["打开"]

# 选中文件地址输入框
dlg["Toolbar3"]

# 选中文件名输入框
dlg["文件名(&N):Edit"]

# 选择打开按钮
dlg["打开(&O)"]
'''

# 使用pywinauto来选择文件 使用pywinautoc创建一个操作桌面窗口的对象
app = pywinauto.Desktop()
# 选择文件上传的窗口
dlg = app["打开"]
time.sleep(5)
# 选择文件地址输入框，点击激活
dlg["Toolbar3"].click()
# 键盘输入上传文件的路径
time.sleep(5)

send_keys(r"C:\Users\liu\Desktop\test")
# 键盘输入回车，打开该路径
send_keys("{VK_RETURN}")
time.sleep(5)
# 选中文件名输入框，输入文件名
dlg["文件名(&N):Edit"].type_keys("111111111.xls")
time.sleep(5)
# 点击打开
dlg["打开(&O)"].click()

time.sleep(5)



