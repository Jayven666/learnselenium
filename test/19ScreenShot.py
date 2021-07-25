# 截图
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(3)
driver.get_screenshot_as_file("D:/软件测试/day21_5.16/截图.png")
driver.quit()
