from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("file:///home/lzy/my_selenium/day1/lzy02/%E5%A4%9A%E6%A0%87%E7%AD%BE%E9%A1%B5%E5%88%87%E6%8D%A2%E5%88%B0%E8%87%AA%E5%88%B6%E7%BD%91%E9%A1%B5.html")
driver.maximize_window()
# current = driver.current_window_handle#获取当前窗口句柄
# print( current)#获取当前窗口句柄
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"精彩")]'))).click()#等待元素加载
# handles = driver.window_handles#获取所有窗口句柄，返回值是列表
# print( handles)
# driver.switch_to.window(handles[1])#切换到新窗口
# wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="仙人模式动图.gif"]')))#等待图片
wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"精彩")]'))).click()#等待元素加载打开超链接
sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="./files/博人头像.png"]'))).click()#等待元素加载打开超链接
sleep(1)
handles = driver.window_handles#获取所有窗口句柄，返回值是列表
for i in handles:#循环所有窗口句柄
    driver.switch_to.window(i)#切换到新窗口
    if driver.title == '博人':#判断标题
        print(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@src="博人.jpeg"]'))).tag_name)#获取图片标签名
        sleep(1)
        break
else:
    print('没有找到博人')
