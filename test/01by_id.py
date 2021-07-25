# find_element_by_id通过id去定位某一个控件
# 1.从selenium库导入webriver模块
from selenium import webdriver
# 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
driver = webdriver.Chrome()
# 3.调用get()方法打开url地址，对象名.方法名
driver.get("http://101.133.169.100/yuns/index.php")
# 4.最大化窗口
driver.maximize_window()
# 5.对象名.find_element_by_id("id属性值")，定位控件中的第1种方式；
# .click()方法实现点击的动作
driver.find_element_by_id("cart_numaaa").click()

