from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.runoob.com/python/python-tutorial.html")
loc = (By.XPATH,"//img[@src='https://static.runoob.com/images/re/kkb20190819/Python3.png']")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


time.sleep(5)
driver.quit()