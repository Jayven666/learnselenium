# find_elements_by_tag_name定位控件中的第8种方式，找的是标签类型div、span……
# 很少用，不精确，一个页面有大量的div等标签，默认是找第一个标签
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(2)

# 把当前页面中所有的div标签找出来存入a列表中
a = driver.find_elements_by_tag_name('div')
print(a)
print(len(a))   # 175


