# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/9/5 17:25
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r'file:///E:/001%20%E4%B8%8A%E8%AF%BE%E8%AF%BE%E4%BB%B6--51testing/002%20selenium%E8%AF%BE%E4%BB%B6/%E5%A4%9A%E6%A0%87%E7%AD%BE%E9%A1%B5%E5%88%87%E6%8D%A2--html/%E5%A4%9A%E6%A0%87%E7%AD%BE%E9%A1%B5%E5%88%87%E6%8D%A2%E5%88%B0%E8%87%AA%E5%88%B6%E7%BD%91%E9%A1%B5.html')
driver.find_element_by_css_selector('.title-text').click()
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "鸣人":
        break

driver.find_element_by_id('text').send_keys('鸣人')

input('Plz :')
driver.quit()


