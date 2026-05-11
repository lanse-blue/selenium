from time import sleep

from selenium import webdriver
driver = webdriver.Chrome ()
driver.maximize_window()
driver.get ("https://www.atstudy.com")
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")
sleep(5)
driver.quit()

