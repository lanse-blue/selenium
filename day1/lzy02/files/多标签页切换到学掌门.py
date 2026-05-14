# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/9/5 16:27

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(r'G:\Python_scripts\UITest\css选择器高级用法\多标签切换.html')
driver.find_element_by_css_selector('.title-text').click()
handles = driver.window_handles   # 获取所有页面的句柄 ，结果是一个列表
for handle in handles:
    driver.switch_to.window(handle)
    if driver.current_url == "https://www.atstudy.com/":
        break

print (driver.title)
print (driver.current_url)
driver.find_element_by_css_selector('.el-button.pre.el-button--text > span').click()

input('Plz input a num:')
driver.quit()
