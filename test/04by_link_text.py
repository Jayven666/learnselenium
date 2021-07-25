# find_element_by_link_text通过a标签的href链接地址去定位某一个控件
# 1.从selenium库导入webriver模块
from selenium import webdriver
import time
# 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
driver = webdriver.Chrome()
# 3.调用get()方法打开url地址，对象名.方法名
driver.get("http://101.133.169.100/yuns/index.php")
# 4.推迟执行2秒钟
time.sleep(2)
# 5.对象名.find_element_by_link_text("a标签中间加的值")，定位控件中的第4种方式；
# .click()方法实现点击的动作
driver.find_element_by_link_text("家装节").click()

