# 时间控件
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
driver.maximize_window()
time.sleep(3)

# 先定位到时间控件
ele = driver.find_element_by_id("HD_CheckIn")
# 清除原本默认值
ele.clear()
# 按页面中的时间格式输入时间
ele.send_keys("2021-05-18")
time.sleep(3)

driver.quit()
