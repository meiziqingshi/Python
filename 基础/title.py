# coding = uft-8
# Author:jin

from selenium import webdriver
import time
from selenium.webdriver.support import  expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.imooc.com")
title_name = driver.title
if "慕课网" in title_name:
    print("打开正确")
else:
    print("不通过")
time.sleep(5)


print(EC.title_contains("慕课网"))

title_a = EC.title_contains("11")
print(title_a(driver))

print(driver)


driver.close()