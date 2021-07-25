# 鼠标事件
# 先导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()
time.sleep(2)

ele = driver.find_element_by_link_text("母婴玩具")
time.sleep(2)

ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# 鼠标移动到了之后才能进行下一步的点击
driver.find_element_by_link_text("营养辅食").click()

# 鼠标右击控件
ActionChains(driver).context_click(ele).perform()
# 鼠标双击控件
ActionChains(driver).double_click(ele).perform()

# 鼠标拖动控件移动多少像素点
driver = webdriver.Chrome()
driver.get('https://www.huodongxing.com/login?ReturnUrl=%2f')
driver.maximize_window()
time.sleep(2)
# 定位控件
driver.find_element_by_class_name("geetest_radar_tip").click()
time.sleep(2)
source = driver.find_element_by_xpath('//div[@class="geetest_slider_button"]')
# x方向传100个像素点，y方向没有拖动所以传0
ActionChains(driver).drag_and_drop_by_offset(source, 200, 0).perform()
# 把控件拖动到指定的目的地
# 定位目的地
# target = driver.find_element_by_xpath('//div[@class="geetest_slider_tip geetest_fade"]')
# ActionChains(driver).drag_and_drop(source, target)
time.sleep(2)
driver.quit()
