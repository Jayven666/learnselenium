# find_element_by_css_selector定位控件中的第7种方式
# 绝对路径：从根节点开始，一层一层往下找到想定位的标签
# css_selector的绝对路径：一般以左斜杠/开头大于号>分隔  html>body>div>div>div>div>form>input
# 相对路径：
# 1、标签中有id属性时可以写成：标签类型#id属性值，（标签类型可省略）如：i#cart_num
# 2、标签中有class属性时可以写成：标签类型.class属性值，如：input.but1
# 3、标签中没有id、class属性时可以写成：标签类型[属性值=""]，如：input[placeholder="请输入你要查找的关键字"]
# 4、连接多个属性值：input[class="but1"][placeholder="请输入你要查找的关键字"][]
# 5、父级找子级：div.schbox>form>input:nth-child(1)  :nth-child(?)确定是第几个子级，类似xpath中的[1]
# 6、定位第一个子级：  :first-child
# 7、定位最后一个子级： :last-child
# 8、定位倒数第几个子级：    :nth-last-child(?)
# 9、对于css_selector来说，第几个子级不是指同标签的顺序而是指父级下所有标签排序的顺序；xpath是相同标签的才进行排序
from selenium import webdriver
import time
time.sleep(2)

driver = webdriver.Chrome()
driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(2)

driver.find_element_by_css_selector("html>body>div>div>div>div>form>input").send_keys("测试xpath")


