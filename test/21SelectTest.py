# 下拉选择框
# 导入Select类
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
driver.maximize_window()
time.sleep(3)

# 定位下拉选择框
s = driver.find_element_by_id("J_roomCountList")
# 方式一：选择文本信息
Select(s).select_by_visible_text("2间")
time.sleep(3)

# 方式二：通过索引从0开始，选择第4间
Select(s).select_by_index(3)
time.sleep(3)

# 方式三：通过value，选择第5间
Select(s).select_by_value("5")

driver.quit()
