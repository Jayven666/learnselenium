# 多窗体处理
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 定位百度输入框输入123并定位搜索按钮点击，此时还只有一个窗体
driver.find_element_by_id("kw").send_keys("123")
driver.find_element_by_id("su").click()
driver.maximize_window()

# 打印日志信息
print(driver.window_handles)
time.sleep(5)

# 点击“hao123”，新打开了一个窗体
driver.find_element_by_link_text("hao123_上网从这里开始").click()
time.sleep(5)
print(driver.window_handles)

# 获取当前窗体的句柄或焦点信息，仍在第一个窗体
print(driver.current_window_handle)

# 切换窗体
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)

driver.quit()
