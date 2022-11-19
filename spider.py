from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
os.environ['PATH'] += r'/Users/justinpak/Desktop/Python/Selenium\Drivers'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import keypair

driver = webdriver.Chrome(options=chrome_options)


def log_in ( user=keypair.user, pasw=keypair.pasw ):
  driver.get('https://www.twitter.com/i/flow/login')
  sleep(2)
  user_in = driver.find_element(by=By.TAG_NAME, value='input')
  user_in.send_keys(user)
  user_in.send_keys(Keys.ENTER)
  sleep(2)
  pasw_in = driver.find_element(by=By.NAME, value='password')
  pasw_in.send_keys(pasw)
  pasw_in.send_keys(Keys.ENTER)

log_in()