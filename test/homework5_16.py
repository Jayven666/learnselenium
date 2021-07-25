# xpath绝对路径3个demo
# # 1.百度搜索框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span[1]/input").send_keys("测试xpath")
# # 2.google翻译输入框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://translate.google.cn/")
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/c-wiz/div/div/c-wiz/div/c-wiz/div/div/div/c-wiz/span/span/div/textarea").send_keys("测试xpath")
# # 3.google翻译“文档”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://translate.google.cn/")
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/c-wiz/div/div/c-wiz/div/nav/div[2]/button").click()

# xpath相对路径15个demo
# # 1.百度输入框-正常情况
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys("测试xpath")
# # 2.百度识图按钮-正常情况
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//span[@class="soutu-btn"]').click()
# # 3.b站搜索框-正常情况
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.bilibili.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//input[@class="nav-search-keyword"]').send_keys("xpath定位测试")
# # 4.百度热搜第一条-使用and连接多个属性值确定唯一控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//span[@class="title-content-title" and text()="辽宁营口现疫情 多人被问责"]').click()
# # 5.百度下方“关于百度”按钮-使用and连接多个属性值确定唯一控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//a[@class="text-color" and @target="_blank" and text()="关于百度"]').click()
# # 6.斗鱼分区“分区搜索”按钮-使用and连接多个属性值确定唯一控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//input[@class="search-ipt " and @placeholder="分区搜索"]').send_keys("xpath定位测试")
# # 7.斗鱼分区“分区搜索”按钮-使用contains定位包含了xx的控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//input[contains(@placeholder,"分区")]').send_keys("xpath定位测试2")
# # 8.百度热搜第一条-使用contains定位包含了xx的控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//span[contains(text(),"辽宁")]').click()
# # 9.百度下方“关于百度”按钮-使用contains定位包含了xx的控件
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//a[contains(text(),"关于百度")]').click()
# # 10.斗鱼分区“首页”按钮-使用文本信息text定位标签
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//a[text()="首页"]').click()
# # 11.百度“学术”按钮-使用文本信息text定位标签
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//a[text()="学术"]').click()
# # 12.知乎“开通机构号”按钮-使用文本信息text定位标签，*正则匹配
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.zhihu.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//*[text()="开通机构号"]').click()
# # 13.b站搜索框-自身无特殊属性值，用父级去定位子级
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.bilibili.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//div[@class="nav-search"]/form/input').send_keys("xpath定位测试")
# # 14.b站“热门”按钮-自身无特殊属性值，用父级去定位子级
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.bilibili.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//div[@id="primaryPageTab"]/ul/li[3]/a').click()
# # 15.b站“动画”按钮-用子级去定位父级
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.bilibili.com/")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element_by_xpath('//span[text()="动画"]/..').click()

# css_selector绝对路径3个demo
# # 1.“百度一下”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("html>body>div>div>div>div>div>form>span>input:nth-child(1)").click()
# # 2.百度搜索框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("html>body>div>div>div>div>div>form>span>input:nth-child(2)").send_keys("css选择器定位测试")
# # 3.百度左上角“hao123”
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("html>body>div>div>div:nth-child(3)>a:nth-child(2)").click()

# css_selector相对路径15个demo
# # 1.含有id属性值时-京东购物车角标
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("i#shopping-amount").click()
# # 2.含有id属性值时-京东搜索框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("input#key").send_keys("css选择器定位测试")
# # 3.含有class属性值时-京东“新人福利”按钮，跳转登录
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector("a.user_profit_lk:nth-child(1)").click()
# # 4.用标签类型[属性值=""]定位-京东首页“秒杀”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector('a[aria-lable="秒杀"]').click()
# # 5.用标签类型[属性值=""]定位-京东识图按钮，跳转登录
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector('a[class="photo-search-login"]').click()
# # 6.[]连接多个属性值定位-京东“品牌闪购”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# time.sleep(2)
# driver.find_element_by_css_selector('a[class="navitems-lk"][aria-lable="品牌闪购"]').click()
# # 7.通过父级定位子级-斗鱼分区“直播”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('ul.Header-menu>li:nth-child(2)>a').click()
# # 8.通过父级定位子级-斗鱼分区“绝地求生”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('ul.layout-Classify-list>li:nth-child(2)>a').click()
# # 9.定位第一个子级-斗鱼分区“英雄联盟”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('li.layout-Classify-item:first-child>a').click()
# # 10.定位第一个子级-斗鱼分区“分区搜索”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('div.search>input:first-child').send_keys("css选择器定位测试")
# # 11.定位最后一个子级-斗鱼分区“正能量”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('a.layout-Module-label:last-child').click()
# # 12.定位倒数第几个子级-斗鱼分区“正能量”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('a.layout-Module-label:nth-last-child(1)').click()
# # 13.定位倒数第几个子级-斗鱼分区“欢乐斗地主”按钮
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.douyu.com/directory")
# time.sleep(2)
# driver.find_element_by_css_selector('li.layout-Classify-item:nth-last-child(40)').click()
# # 14.多个不同标签下的序号问题-云商系统登陆页面用户名输入框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("http://101.133.169.100/yuns/index.php/member/login")
# time.sleep(2)
# driver.find_element_by_css_selector('div.bcon>div:nth-child(2)>input').send_keys("css选择器定位测试")
# # 15.多个不同标签下的序号问题-百度输入框
# from selenium import webdriver
# import time
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# driver.find_element_by_css_selector('form#form>span:nth-child(8)>input').send_keys("css选择器定位测试")

# 面试问题：在写自动化代码中你一般喜欢用什么定位方式，为什么？
# 如果能用id/name/class的话优先使用，效率会高一些；xpath是按DOM树去解析的，效率会低一些；
# 如果说没有id/name/class或者不唯一时则会考虑使用xpath，因为xpath可以定位到所有的控件

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
time.sleep(2)
driver = webdriver.Chrome()
driver.get("http://101.133.169.100:8088/index.html#/login")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(
            "13676083391")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('//div[text()="客户管理"]').click()
time.sleep(15)
# 进入客户模块
ele_ul = driver.find_elements_by_xpath('//ul[@class="el-menu-vertical el-menu"]/a/li')
ele_ul[3].click()
time.sleep(5)
# 定位到搜索框
ele_input = driver.find_element_by_xpath('//input[@placeholder="请输入客户名称/手机/电话"]')
ele_input.click()
# 输入搜索内容
ele_input.send_keys("张三")
# 点击搜索
driver.find_element_by_xpath('//i[@class="el-icon-search"]').click()
# 定位搜索后的内容
time.sleep(3)
el = driver.find_elements_by_xpath("//div[@class='cell el-tooltip']")
# 循环遍历
for i in range(0, len(el)):
    print("第" + str(i) + "个=" + el[i].text)
# 断言结果,根据输入框文本信息是否包含，断言搜索后的内容


