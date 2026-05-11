from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import *
my_driver = webdriver.Edge ()
my_driver.get ("file:///home/lzy/example.html")
str =  "Dream of the Red Chamber"
str_lst = str.split(" ")
class_name_str = str_lst[randint(0,len(str_lst)-1)]
emt = my_driver.find_element(By.CLASS_NAME,class_name_str)
if emt.is_enabled():
    emt.send_keys("I Love You")
else:
    print("Element is disabled")
sleep(5)
my_driver.quit()
2
driver = webdriver.Edge ()
driver.get ("file:///home/lzy/example.html")
elm_lst = driver.find_elements(By.TAG_NAME,"input")
for i in elm_lst:
    if i.get_attribute("type") == 'checkbox' or i.get_attribute("type") == 'radio':
        if not i.is_selected():
            i.click()
            sleep(4)
    else:
        if i.is_enabled():
            i.send_keys("I Love You")
            sleep(4)
        else:
            print("Element is disabled")
            sleep(4)