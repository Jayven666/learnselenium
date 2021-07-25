# 键盘事件
# 先导入keys类
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(2)

# 输入框输入内容后按退格键删除
driver.find_element_by_class_name("but1").send_keys("键盘事件")
driver.find_element_by_class_name("but1").send_keys(Keys.BACK_SPACE)
time.sleep(2)
# 输入空格键
driver.find_element_by_class_name("but1").send_keys(Keys.SPACE)
driver.find_element_by_class_name("but1").send_keys("and")
time.sleep(2)
# 输入回车键
driver.find_element_by_class_name("but1").send_keys(Keys.ENTER)
# 全选、复制、剪切、粘贴
driver.find_element_by_class_name("but1").send_keys(Keys.CONTROL, "a")
time.sleep(2)
driver.find_element_by_class_name("but1").send_keys(Keys.CONTROL, "c")
time.sleep(2)
driver.find_element_by_class_name("but1").send_keys(Keys.CONTROL, "x")
time.sleep(2)
driver.find_element_by_class_name("but1").send_keys(Keys.CONTROL, "v")
time.sleep(2)
driver.quit()
