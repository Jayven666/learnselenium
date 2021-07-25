# 特殊时间控件
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
driver.maximize_window()
time.sleep(3)

# 注入一段js，用removeAttribute移除readonly属性
js = "document.getElementById('noticeEndTime').removeAttribute('readonly')"
js = "document.getElementsByName('noticeEndTime')[0].removeAttribute('readonly')"
js = "document.getElementsByTagName('input')[0].removeAttribute('readonly')"

# 执行js
driver.execute_script(js)
# 移除readonly属性后再输入时间
driver.find_element_by_name("noticeEndTime").send_keys("2021-05-18 01:21:23")
