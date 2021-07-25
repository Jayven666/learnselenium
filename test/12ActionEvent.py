# 动作事件

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(2)

# 输入内容
driver.find_element_by_xpath('//input[@class="but1"]').send_keys("动作事件")
time.sleep(2)
# 清空内容
driver.find_element_by_xpath('//input[@class="but1"]').clear()
time.sleep(2)
# 点击事件
driver.find_element_by_xpath('//a[@title="秒杀"]').click()
time.sleep(2)

driver.quit()
