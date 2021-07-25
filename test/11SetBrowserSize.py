# 窗体大小设置

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(2)

driver.maximize_window()
time.sleep(2)
driver.set_window_size(1600, 900)
time.sleep(2)

driver.quit()
