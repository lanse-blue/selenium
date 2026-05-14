from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("file:///home/lzy/my_selenium/xiala/example.html")
# driver.get(
#     "file:///home/lzy/my_selenium/lzy04/shubiao.html")
# sleep(2)
# driver.find_element(By.ID, 'button3').click()
# hand = driver.switch_to.alert  # 模拟手获取alert对象
# sleep(2)
# print(hand.text)
# sleep(2)
# hand.accept()#模拟点击确定按钮
# sleep(2)

# hand.dismiss()#模拟点击取消按钮
# print(hand.text)
# sleep(2)
# hand.send_keys("lzy")  # 模拟输入
# sleep(2)
# hand.accept()
# input("输入任意字符退出")
# driver.quit()


# 多窗口切换

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)
# driver.get("file:///home/lzy/my_selenium/day1/lzy02/%E5%A4%9A%E6%A0%87%E7%AD%BE%E9%A1%B5%E5%88%87%E6%8D%A2%E5%88%B0%E8%87%AA%E5%88%B6%E7%BD%91%E9%A1%B5.html")
# driver.maximize_window()
# current = driver.current_window_handle#获取当前窗口句柄
# print( current)#获取当前窗口句柄
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"精彩")]'))).click()#等待元素加载
# handles = driver.window_handles#获取所有窗口句柄，返回值是列表
# print( handles)
# driver.switch_to.window(handles[1])#切换到新窗口
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="仙人模式动图.gif"]')))#等待图片
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"精彩")]'))).click()#等待元素加载打开超链接
# sleep(1)
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="./files/博人头像.png"]'))).click()#等待元素加载打开超链接
# sleep(1)
# handles = driver.window_handles#获取所有窗口句柄，返回值是列表
# for i in handles:#循环所有窗口句柄
#     driver.switch_to.window(i)#切换到新窗口
#     if driver.title == '博人':#判断标题
#         print(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="博人.jpeg"]'))).tag_name)#获取图片标签名
#         sleep(1)
#         break
# else:
#     print('没有找到博人')


# 普通框架没有嵌套
# driver.switch_to.frame('secondIframe')  # 使用框架id去切换框架

# driver.switch_to.frame('second')#使用框架name去切换框架

# driver.switch_to.frame(1)#使用索引去切换框架

# emt = driver.find_element(By.CSS_SELECTOR,'#secondIframe')#使用框架元素本身去切换框架
# driver.switch_to.frame(emt)#完成切换框架

# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#button1'))).click()
# sleep(2)
# driver.switch_to.alert.accept()
# sleep(2)

# #嵌套框架
# driver.switch_to.frame('second')  # 从最外层框架切换到中间层框架
# driver.switch_to.frame('third')  # 从中间层切换到最内层框架
#
# wait.until(EC.presence_of_element_located((By.ID, 'atstudy'))).click()
# sleep(2)
#
# # driver.switch_to.parent_frame()#返回上一层框架
# # driver.switch_to.parent_frame()
#
# driver.switch_to.default_content()  # 返回最外层框架
#
# wait.until(EC.presence_of_element_located((By.ID, 'input'))).send_keys('lzy')
# sleep(2)
# input("输入任意字符退出")
# driver.quit()


# 鼠标事件
# 无论哪个鼠标事件操作步骤都一样
# 首先定位鼠标需要操作的元素
# 创建ActionChains对象
# 调用事件方法，之后再调用perform()方法完成操作
# 双击和右键事件

# #双击
# emt1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[value="双击改变内容"]')))
# ActionChains(driver).double_click(emt1).perform()#完成双击ActionChains(driver)实例化对象之后调用类里
# # 的事件方法，这些方法返回的都是对象本身，
# # 所以可以链式调用而不是创建新的对象再调用perform()
# sleep(2)
# #右键
# emt2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[value="在此区域点击右键"]')))
# act = ActionChains(driver)
# act.context_click(emt2).perform()
# sleep(2)
# driver.switch_to.alert.accept()
# input("输入任意字符退出")
# driver.quit()

# #拖动
# driver.switch_to.frame('firstIframe')
# emt1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#blackSquare')))#定位被拖动元素
# emt2 =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#targetEle')))#定位拖动目标元素
# ActionChains(driver).drag_and_drop(emt1,emt2).perform()#完成拖动
# sleep(2)


# # 移动
# emt = wait.until(EC.presence_of_element_located((By.ID, 'blackSquare')))
# emt2 = wait.until(EC.presence_of_element_located((By.ID, 'blackSquare')))
# ActionChains(driver).drag_and_drop_by_offset(emt1, 50, 250).pause(3).drag_and_drop_by_offset(emt2, 200, 250).perform()
# sleep(2)

# #悬停
# emt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="下载APP"]')))
# ActionChains(driver).move_to_element(emt).perform()
# sleep(2)

# # 链式调用
# # 等待登录按钮可点击
# wait.until(
#     EC.presence_of_element_located((By.XPATH, '//*[text()="登录"]'))
# ).click()
# # 等待弹窗中的元素出现
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="密码登录"]'))).click()
# sleep(1)
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="请输入手机号码"]'))).send_keys("13259879962")
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@placeholder="请输入密码"]'))).send_keys("lzy666233.")
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="登录"]'))).click()
# emt1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.bar>img')))
# emt2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="退出登录"]')))
# ActionChains(driver).move_to_element(emt1).pause(3).click(emt2).perform()
# sleep(2)

# 键盘事件
emt1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#IamID[name="first"]')))
emt2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#IamID[name="second"]')))
emt1.send_keys(Keys.BACKSPACE)
emt1.send_keys(Keys.CONTROL, 'a')
sleep(1)
emt1.send_keys(Keys.CONTROL, 'x')
sleep(1)
emt2.send_keys(Keys.CONTROL, 'v')
sleep(1)
emt2.send_keys(Keys.HOME)
sleep(1)
emt2.send_keys(Keys.CONTROL,Keys.SHIFT,Keys.END)
sleep(2)
driver.quit()
