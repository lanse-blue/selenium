from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
def my():
    driver = webdriver.Chrome()
    driver.get ("https://www.atstudy.com")
    driver.maximize_window()
    emt_login=driver.find_element(By.CSS_SELECTOR,'div[class="login"]>button:first-child')
    sleep(3)
    emt_login.click()
    sleep(5)
    emt_phone=driver.find_element(By.CSS_SELECTOR,'[class="pic"]>div:nth-child(2)>p')
    emt_phone.click()
    sleep(5)
    emt_phone_num=driver.find_element(By.CSS_SELECTOR,'[class="phone uni-phone el-input"]>input')
    emt_phone_num.send_keys("13259879962")
    sleep(5)
    emt_password=driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入密码"]')
    emt_password.send_keys("lzy666233.")
    sleep(5)
    emt_login_button=driver.find_element(By.CSS_SELECTOR,'[class="el-button el-button--primary send"]')
    emt_login_button.click()
    sleep(5)
    result = driver.find_element(By.CSS_SELECTOR,'[class="study-center"]>p').text
    driver.quit()
    return result


print(my())