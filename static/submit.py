import sys
import os
import time
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

contest_id = (sys.argv)[1]
task_id = (sys.argv)[2]

url = "https://codeforces.com/contest/"+contest_id+"/problem/"+task_id

driver = webdriver.Chrome('chromedriver')
driver.get(url)
try:
	enter = driver.find_element(By.LINK_TEXT, "Enter")
	enter.click()
	user_name = driver.find_element_by_id("handleOrEmail")
	user_name.send_keys(USER_NAME)
	password = driver.find_element_by_id("password")
	password.send_keys(PASSWORD)
	submit = driver.find_element_by_class_name("submit")
	submit.click()
	time.sleep(10)
except:
	pass

language = driver.find_element_by_name("programTypeId")
language.send_keys("GNU G++17 7.3.0")
sourceFile = driver.find_element_by_name("sourceFile")
sourceFile.send_keys(os.path.abspath("contests/cf_"+str(contest_id)+"/"+task_id+".cpp"))
submit_btn = driver.find_element_by_class_name("submit")
submit_btn.click()

driver.close()