from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

def loggingIn(user_username, user_password):
    link = driver.find_element_by_link_text("Sign in with github")
    link.click()

    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    time.sleep(10)
    username = driver.find_element_by_id("login_field")
    password = driver.find_element_by_id("password")
    username.send_keys(user_username)
    password.send_keys(user_password)
    driver.find_element_by_name("commit").click()
    

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://todo-list-login.firebaseapp.com/")
window_before = driver.window_handles[0]
#type your Github username here
username = "dianacuiting"
#type your Github password here
password = "myparentsandsisrocks"
loggingIn(username, password)
driver.switch_to_window(window_before)

time.sleep(10)
for i in range(11):
    value = randint(0, 100)
    input_list = driver.find_element_by_xpath("//div/div/input[1]")
    input_list.send_keys(value)
    button = driver.find_element_by_xpath("//div/div/button[1]")
    button.click()

sign_out = driver.find_element_by_xpath("//button[1]")
sign_out.click()

link = driver.find_element_by_link_text("Sign in with github")
link.click()
driver.switch_to_window(window_before)

time.sleep(10)
for i in range(6):
    delete_list = driver.find_element_by_xpath("//div/div/ul/li[5]/div/div[2]/button[1]")
    delete_list.click()
    
sign_out = driver.find_element_by_xpath("//button[1]")
sign_out.click()

time.sleep(5)
driver.quit()

