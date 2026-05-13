from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(
    r"file:///home/lzy/my_selenium/lzy01/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0HTML__%E9%9D%9Einput%E6%A0%87%E7%AD%BE%20%E5%92%8C%20input%E6%A0%87%E7%AD%BE.html")
# driver.get(r"file:///home/lzy/example.html")
# driver.get(
#     'file:///home/lzy/my_selenium/xiala/%E9%9D%9Eselect%E6%A0%87%E7%AD%BE%E7%9A%84%E4%B8%8B%E6%8B%89%E6%A1%86.html')
# emt = driver.find_element(By.CSS_SELECTOR,'input#IamID[name="first"].poem')
# emt.clear()
# emt.send_keys("I Love You")
# emt1 = driver.find_element(By.CSS_SELECTOR,'input#IamID[name="second"][class="poem"].poem')
# emt1.send_keys("I Love You1")
# emt2 = driver.find_element(By.CSS_SELECTOR,'input[type="text"]#ID[name="first"].Dream.of')
# emt2.send_keys("I Love You2")
# sleep(3)
# emt3 = driver.find_element(By.CSS_SELECTOR,'form #hongloumeng')#后代选择器
# print(emt3.text)
# emt4 = driver.find_element(By.CSS_SELECTOR,'form>span>#title6')#子代选择器
# # print(emt4.text)
# emt5 = driver.find_element(By.CSS_SELECTOR,'option:nth-last-child(2)')
# print(emt5.text)
# emt6 = driver.find_element(By.CSS_SELECTOR,'option:nth-child(2)')
# print(emt6.text)
# emt7 = driver.find_element(By.CSS_SELECTOR,'option:first-child')
# print(emt7.text)
# emt8 = driver.find_element(By.CSS_SELECTOR,'option:last-child')
# print(emt8.text)
# # xpath索引定位
# driver.find_element(By.XPATH, '(//input)[1]').send_keys('xpath索引定位')
# # xpath属性定位全部属性值
# driver.find_element(By.XPATH,
#                     '//input[@class="Dream of the Red Chamber"][@description="Dream of the Red Chamber 是红楼梦的英文翻译"]').send_keys(
#     'xpath属性定位')
# sleep(3)
# # xpath属性包含定位
# driver.find_element(By.XPATH, '//input[contains(@description,"the")]').send_keys('xpath属性包含定位')
# sleep(3)
# # xpath属性开始定位
# driver.find_element(By.XPATH, '//input[starts-with(@description,"D")]').send_keys('xpath属性开始定位')
# sleep(3)
# # xpath文本定位的全部文本定位
# driver.find_element(By.XPATH, '(//a)[text()="请点击，进入学掌门"]').click()
# sleep(3)
# driver.back()
# sleep(3)
# # xpath文本定位的部分文本定位
# driver.find_element(By.XPATH, '//a[contains(text(),"点击")]').click()
# sleep(3)
# driver.back()
# sleep(3)
# # xpath文本定位的开头文本定位
# driver.find_element(By.XPATH, '//a[starts-with(text(),"请")]').click()
# sleep(3)
# driver.back()
# sleep(3)
# 路径通配符
# # 并且使用逻辑运算符组合表达式定位元素
# print(driver.find_element(By.XPATH, '//*[@id="tianshang" and text()="我是span标签"]').text)
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, 'div#options>input').click() # css 标签id属性以及子代选择器定位
# sleep(3)
# driver.find_element(By.XPATH, '//*[text()="黄色"]').click()# xpath 文本定位的全部文本定位
# sleep(3)
# emt = driver.find_element(By.ID, 'poem')
# Select(emt).select_by_visible_text('红豆生南国，春来发几枝。')  # 使用select_by_visible_text()方法直接对子元素进行操作 文本内容
# sleep(3)
# Select(emt).select_by_index(2)  # 使用select_by_index()方法对子元素进行操作 索引
# sleep(3)
# Select(emt).select_by_value('third')  # 使用select_by_value()方法对子元素进行操作  value属性值
sleep(3)
emt = driver.find_element(By.ID, 'fuMain')
file_path = r'/home/lzy/my_selenium/lzy01/files/scenery.jpg'
emt.send_keys(file_path)  # 通过send_keys()方法上传文件
sleep(5)
pyautogui.click()


driver.set_window_size(920, 500)
sleep(3)
driver.quit()
