from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome ()
driver.get ("https://www.atstudy.com")
driver.maximize_window()
sleep(2)
#截图
driver.get_screenshot_as_file('jietu1.png')
sleep(2)
print(driver.get_screenshot_as_base64())#截图以base64编码字符串显示
print(driver.get_screenshot_as_png())#截图png以二进制数据显示
driver.save_screenshot('jietu1.png')
#元素截图
emt = driver.find_element(By.CSS_SELECTOR,'[alt="logo"]')
emt.screenshot('logo1.png')
sleep(2)
driver.quit()