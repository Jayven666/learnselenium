# 控制浏览器的几种方法

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.find_element_by_link_text("9.9抢大牌").click()
time.sleep(2)

# 刷新页面
driver.refresh()
time.sleep(2)
# 后退页面
driver.back()
time.sleep(2)
# 前进页面
driver.forward()
time.sleep(2)

driver.quit()


