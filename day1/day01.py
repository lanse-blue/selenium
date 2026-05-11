from selenium import webdriver  # 导入
from time import *

my_driver = webdriver.Firefox()  # 创建对象
my_driver.get('file:///C:/Users/Administrator/Desktop/example.html')  # 使用get方法打开网站
# print(my_driver.current_url)#获取网址
# print(my_driver.page_source)#获取源代码
# print(my_driver.title)#获取标题
# input('zuse')#阻塞运行
# emt = my_driver.find_element_by_id('IamID')#定位元素并且创建对象
# emt.click()#调用click方法点击元素
# sleep(3)
# emt.clear()#调用clear方法清除
# sleep(3)
# emt.send_keys('1234567')#调用方法输入
# sleep(3)
# print(emt.get_attribute('name'))
# sleep(3)
# print(emt.get_attribute('class'))
# sleep(3)
# print(emt.is_enabled())#能否编辑
# print(emt.is_displayed())#能否显示在前端界面
# emt = my_driver.find_element_by_id('scroll')
# print(emt.text)#获取元素的文本属性
# print(emt.tag_name)#获取元素的标签属性
# emt1 = my_driver.find_element_by_id('hongloumeng')#通过id定位
# print(emt1.text)#获取元素的文本属性
# sleep(3)
# emt2 = my_driver.find_element_by_name('second')#通过name定位
# emt2.send_keys('name属性定位')
# sleep(3)
# emt3 = my_driver.find_element_by_class_name('RedChamber')#通过class_name定位没有空格直接使用
# emt3.send_keys('class_name属性定位')
# sleep(3)
# emt4 = my_driver.find_element_by_class_name('Chamber')#有空格使用其中一个子属性
# emt4.send_keys('通过class中的一个子属性定位')
# sleep(3)
# emt1 = my_driver.find_element_by_css_selector('#IamID')
# emt1.clear()#
# sleep(3)
# emt2 = my_driver.find_element_by_xpath('//*[@id="IamID"]')
# emt2.send_keys('通过xpath定位')
# sleep(3)
# emt2.clear()
# emt3 = my_driver.find_element_by_tag_name('input')
# emt3.send_keys('通过tag_name定位')
# sleep(3)
# emt1 = my_driver.find_element_by_link_text('唐•李白')
# print(emt1.get_attribute('value'))
# emt2 = my_driver.find_element_by_partial_link_text('三五8377iuhih')
# print(emt2.get_attribute('id'))
# print(emt2.text)
# print(emt2.tag_name)
# emts = my_driver.find_elements_by_partial_link_text('白')
# print(emts)
# for i in emts:
#     print(i.text,i.tag_name)
emts = my_driver.find_elements_by_tag_name('wkhekqwkelhha')
print(emts)
# n = 1
# print(len(emts))
# for i in emts:
#     print(f'第{n}个超链接的文本内容是{i.text}')
#     n+=1
my_driver.quit()  # 关闭浏览器
