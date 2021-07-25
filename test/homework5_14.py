# # 京东-find_element_by_id通过id去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.jd.com/")
# # 4.最大化窗口
# driver.maximize_window()
# # 5.对象名.find_element_by_id("id属性值")，定位控件中的第1种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_id("settleup").click()

# # b站-find_element_by_id通过id去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.bilibili.com/")
# # 4.最大化窗口
# driver.maximize_window()
# # 5.对象名.find_element_by_id("id属性值")，定位控件中的第1种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_id("reportFirst1").click()
#
# # 智联招聘-find_element_by_id通过id去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.zhaopin.com/")
# # 4.最大化窗口
# driver.maximize_window()
# # 5.对象名.find_element_by_id("id属性值")，定位控件中的第1种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_id("slider1").click()

# # 百度—find_element_by_name通过name去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.baidu.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_name("name属性值")，定位控件中的第2种方式；
# # .send_keys()方法实现给输入框输入内容
# # name的属性值有可能是重复的，如果重复将会查找第一个
# driver.find_element_by_name("wd").send_keys("定位到了输入框")

# # 网易云—find_element_by_name通过name去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://music.163.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_name("name属性值")，定位控件中的第2种方式；
# # .send_keys()方法实现给输入框输入内容
# # name的属性值有可能是重复的，如果重复将会查找第一个
# driver.find_element_by_name("srch").send_keys("定位到了输入框")

# # 淘宝—find_element_by_name通过name去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.taobao.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_name("name属性值")，定位控件中的第2种方式；
# # .send_keys()方法实现给输入框输入内容
# # name的属性值有可能是重复的，如果重复将会查找第一个
# driver.find_element_by_name("q").send_keys("定位到了输入框")

# # 淘宝-find_element_by_class_name通过class去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.taobao.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_class_name("name属性值")，定位控件中的第3种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_class_name("search-imgsearch-upload").click()

# # 百度-find_element_by_class_name通过class去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.baidu.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_class_name("name属性值")，定位控件中的第3种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_class_name("soutu-btn").click()

# # 知乎-find_element_by_class_name通过class去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.zhihu.com/explore")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_class_name("name属性值")，定位控件中的第3种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_class_name("ExploreHomePage-specialsLoginBottomButton").click()

# # 百度-find_element_by_link_text通过a标签的href链接地址去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.baidu.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_link_text("a标签中间加的值")，定位控件中的第4种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_link_text("新闻").click()

# # 慕课网-find_element_by_link_text通过a标签的href链接地址去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.imooc.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_link_text("a标签中间加的值")，定位控件中的第4种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_link_text("免费课").click()

# # 慕课网-find_element_by_partial_link_text通过部分唯一的连续文本信息去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.imooc.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_partial_link_text("部分唯一、连续的文本信息")，定位控件中的第5种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_partial_link_text("课教").click()

# # 斗鱼-find_element_by_partial_link_text通过部分唯一的连续文本信息去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://www.douyu.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_partial_link_text("部分唯一、连续的文本信息")，定位控件中的第5种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_partial_link_text("综合").click()

# # 凤凰网-find_element_by_partial_link_text通过部分唯一的连续文本信息去定位某一个控件
# # 1.从selenium库导入webriver模块
# from selenium import webdriver
# import time
# # 2.初始化webdriver类的一个对象命名为driver，操作chrome浏览器
# driver = webdriver.Chrome()
# # 3.调用get()方法打开url地址，对象名.方法名
# driver.get("https://news.ifeng.com/")
# # 4.推迟执行2秒钟
# time.sleep(2)
# # 5.对象名.find_element_by_partial_link_text("部分唯一、连续的文本信息")，定位控件中的第5种方式；
# # .click()方法实现点击的动作
# driver.find_element_by_partial_link_text("调水，总书记").click()







