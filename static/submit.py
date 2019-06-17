import sys
import os
import time
from credentials import USER_NAME, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

contest_id = (sys.argv)[1]
task_id = (sys.argv)[2]

url = "https://codeforces.com/contest/"+contest_id+"/problem/"+task_id

try:
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
except:
	print("<span id='close_pop_up'>&times;</span><h5 style='color:red;'>Chrome Webdriver Error</h5><p>Chrome webdriver cannot be initiated</p><p>For manual submit, <a href='https://codeforces.com/contest/"+str(contest_id)+"/submit/"+task_id+"' target='_blank' style='color:#7fff00;font-weight:bold;text-decoration:none;'>CLICK HERE</a></p>")
	sys.exit()
	
try:
	driver.get(url)
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
	print("<span id='close_pop_up'>&times;</span><h5 style='color:#fa4a4a;'>Network Error / Site is not available</h5>")
	sys.exit()
	

flag = 0
try:
	error_source_file = driver.find_element_by_class_name("shiftUp")
	flag = 1
except:
	pass
if flag:
	print("<span id='close_pop_up'>&times;</span><h5 style='color:#fa4a4a;'>Invalid Login Credentials</h5><p>Please enter valid credentials in static/credentials.py</p>")
	sys.exit()

try:
	language = driver.find_element_by_name("programTypeId")
	language.send_keys("GNU G++17 7.3.0")
	sourceFile = driver.find_element_by_name("sourceFile")
	sourceFile.send_keys(os.path.abspath("contests/cf_"+str(contest_id)+"/"+task_id+".cpp"))
	submit_btn = driver.find_element_by_class_name("submit")
	submit_btn.click()
except:
	print("<span id='close_pop_up'>&times;</span><h5 style='color:#fa4a4a;'>Submission Error</h5><p>"+task_id+".cpp cannot be submitted</p><p>For manual submit, <a href='https://codeforces.com/contest/"+str(contest_id)+"/submit/"+task_id+"' target='_blank' style='color:#7fff00;font-weight:bold;text-decoration:none;'>CLICK HERE</a></p>")
	sys.exit()

try:
	error_source_file = driver.find_element_by_class_name("shiftUp")
	print("<span id='close_pop_up'>&times;</span><h5 style='color:#fa4a4a;'>Same Solution Error</h5><p>You are trying to submit exactly the same code before</p><p>Please visit <a href='https://codeforces.com/contest/"+str(contest_id)+"/my' target='_blank' style='color:#7fff00;font-weight:bold;text-decoration:none;'>My Submissions</a></p>")
except:
	print("<span id='close_pop_up'>&times;</span><h5>Solution Submitted</h5><p>Please visit <a href='https://codeforces.com/contest/"+str(contest_id)+"/my' target='_blank' style='color:#7fff00;font-weight:bold;'>My Submissions</a></p>")

driver.close()