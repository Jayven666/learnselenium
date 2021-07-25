# find_element_by_xpath定位控件中的第6种方式
# 绝对路径：从根节点开始，一层一层往下找到想定位的标签
# xpath的绝对路径：一般以左斜杠/开头  /html/body/div/div/div/div/form/input[1]
# 当确定xpath路径是唯一的之后再往代码里面写
# from selenium import webdriver
# import time
# time.sleep(2)
#
# driver = webdriver.Chrome()
# driver.get("http://101.133.169.100/yuns/index.php")
# time.sleep(2)
#
# driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("测试xpath")

# 相对路径：从中间具有特殊属性的某一个层级找起从而定位到想要定位的标签
# xpath的相对路径：一般以双左斜杠//开头    //input[@class="but1"]
# 情况1：通过某一个属性定位不到唯一值，用and连接多个属性 //input[@name="key" and @type="text" and @placeholder="请输入你要查找的关键字"]
# 情况2：定位动态变化的标签时，想要定位的属性值只要包含了xxx那么就是我想要定位的标签 //input[contains(@placeholder,"请输入")]
# 情况3：通过文本信息去定位控件, *：正则匹配，不管什么标签中间有加文本text //*[text()="家装节"]
# 情况4：自身没有特殊属性时通过父级去定位子级    //div[@class="sch"]/div/form/input[1]
# 情况5：通过子级定位父级  //input[@class="but1"]/..   通过input定位到了form标签
from selenium import webdriver
import time
time.sleep(2)

driver = webdriver.Chrome()
driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(2)

driver.find_element_by_xpath('//input[@name="key" and @type="text" and @placeholder="请输入你要查找的关键字"]').send_keys("测试xpath")



