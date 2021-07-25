# 等待时间
# 先导入keys类
from time import sleep
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
# 打开页面等待2s让页面完全加载出来
time.sleep(2)

# # 输入框输入内容后等待2s
# driver.find_element_by_class_name("but1").send_keys("强制等待时间")
# time.sleep(2)
#
# # 隐式等待时间：写了10s但是如果控件3s就加载出来了那就只需要等待3s
# driver.implicitly_wait(10)
# driver.find_element_by_class_name("but1").send_keys("隐式等待时间")
# time.sleep(2)
# driver.find_element_by_class_name("but1").send_keys("!!!")
# time.sleep(2)

# 显式等待时间
ele = WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located(
    (By.XPATH, '//input[@class="but1"]')))
ele.send_keys("显式等待时间")
time.sleep(3)

driver.quit()
