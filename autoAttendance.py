# coding:utf-8

"""自動で出退勤打刻をする"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

def browser_init():
  chrome_options = Options()
  chrome_options.add_argument("--allow-running-insecure-content")
  chrome_options.add_argument("--allow-insecure-websocket-from-https-origin")
  chrome_options.add_argument("allow-outdated-plugins")
  driver = webdriver.Chrome("/Users/fndm52/study_python/chromedriver", chrome_options=chrome_options)
  return driver

def login():
  driver.get("https://login.salesforce.com")
  inputUserName = driver.find_element_by_css_selector("#username")
  inputPassWord = driver.find_element_by_css_selector("#password")
  loginBtn = driver.find_element_by_css_selector("#Login")
  inputUserName.send_keys("user nameを入れる")
  inputPassWord.send_keys("パスワードをいれる")
  loginBtn.click()

def openBtnPanel():
  driver.implicitly_wait(5000)
  driver.find_element_by_css_selector('a[title="勤怠打刻"]').click()

def click_attendance_btn():
  driver.implicitly_wait(6000)
  driver.switch_to.frame(driver.find_element_by_css_selector("[title=Ts1PushTimeView]"))
  now = datetime.now().strftime("%H")
  if int(now) >= "定時の退勤時間":
    driver.find_element_by_id('pushEnd').click()
  else:
    driver.find_element_by_id('pushStart').click()

driver = browser_init()
login()
openBtnPanel()
click_attendance_btn()
