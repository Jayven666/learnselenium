# alert弹出框
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file://D:\\软件测试\\day21_5.16\\testAlert.html')
driver.maximize_window()
time.sleep(8)
driver.execute_script("prom()")
time.sleep(3)

# 在alert的输入框输入内容，获取文本信息
driver.switch_to.alert.send_keys("test")
time.sleep(3)
print(driver.switch_to.alert.text)

# 点击alert上的确定按钮
driver.switch_to.alert.accept()
print(driver.switch_to.alert.text)
time.sleep(4)
driver.switch_to.alert.accept()
# 点击aleert上的取消按钮
# driver.switch_to.alert.dismiss()

# driver.quit()
