# 滚动条处理
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://qiye.163.com/')
driver.maximize_window()
time.sleep(3)

# 注入一段js，用removeAttribute移除readonly属性
js = "var q=document.documentElement.scrollTop=10000"

# 执行js
driver.execute_script(js)
time.sleep(3)

# 滚动到窗体高度的50%
driver.execute_script("winodw.scrollTo(0, document.body.scrollHeight*0.5)")
time.sleep(3)

# 相对当前坐标移动多少坐标
driver.execute_script("winodw.scrollBy(0, -200)")

