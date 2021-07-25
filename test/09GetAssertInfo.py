# 获取验证信息
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(2)

# 获取title信息
title = driver.title
print(title)

# 获取“联系客服”页面的url地址
# 1.先跳转“联系客服页面”
driver.find_element_by_link_text("联系客服").click()
# 2.获取url信息
url = driver.current_url
print(url)


