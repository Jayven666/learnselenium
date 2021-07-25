# 获取属性方法

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(2)

# .size获取输入框的高和宽
size = driver.find_element_by_xpath('//input[@class="but1"]').size
# 打印size类型，字典
print(type(size))
# 字典内容：高和宽
print(size)
# 字典中根据key取value
print(size["height"])
time.sleep(2)

# .text获取控件上的文本信息
text = driver.find_element_by_xpath('//div[@class="top"]/span').text
print(text)

# .get_attribute获取控件上属性对应的属性值
attr = driver.find_element_by_xpath('//input[@class="but1"]').get_attribute("placeholder")
print(attr)

# .is_displayed()判断控件是否已经显示出来
dis = driver.find_element_by_xpath('//input[@class="but1"]').is_displayed()
print(dis)
if dis:
    driver.find_element_by_xpath('//input[@class="but1"]').send_keys("控件已经显示出来了")
    # .get_arrtibute("value")判断输入内容后回显的值是否一致，固定传value
    txt = driver.find_element_by_xpath('//input[@class="but1"]').get_attribute("value")
    print(txt)
else:
    time.sleep(10)
    driver.find_element_by_xpath('//input[@class="but1"]').send_keys("控件已经显示出来了")

driver.quit()
