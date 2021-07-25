# iframe
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=js_prompt')
driver.maximize_window()
time.sleep(3)

# 有id和name属性且有属性值时
driver.switch_to.frame("iframeResult")
driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
time.sleep(3)

# 没有id和name时
iframe = driver.find_element_by_xpath('//div[@id="iframewrapper"]/iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
time.sleep(3)

# 子级iframe切到父级ifreame
driver.switch_to.parent_frame()
# 切回主文档
driver.switch_to.default_content()

driver.quit()
