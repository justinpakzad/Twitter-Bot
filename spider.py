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
import pandas as pd  
import csv
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
usernames = []
# Getting usernames 
while True:   
    users = driver.find_elements(by=By.TAG_NAME, value='article')
    for u in users:
        u.send_keys(Keys.PAGE_DOWN)
        tweet = u.find_elements(by=By.TAG_NAME, value='span')
        for t in tweet:
            if t.text.startswith('@') and t.text != '@solucky__games':
                usernames.append(t.text)
    break
user_names = set(usernames)
# user_names = sorted(usernames)



# Getting Wallets
driver.get('https://twitter.com/solucky__games/status/1522200777829367809')
walletz = []
while True:
    wallets = driver.find_elements(by=By.TAG_NAME, value='article')
    for w in wallets:
        w.send_keys(Keys.PAGE_DOWN)
        wal = w.find_elements(by=By.TAG_NAME, value='span')
        for wa in wal:
            if len(wa.text) >32 and len(wa.text) >= 44: 
                walletz.append(wa.text)   
    break
walletz
driver.refresh()
wallz =  set(walletz)
len(walletz)

# Writing to csv
dicty = {'username':user_names}
df = pd.DataFrame(dicty) 
df.to_csv('So_Lucks.csv')

d = {'wallets':walletz}
datafram = pd.DataFrame(d)
datafram.to_csv('So_lucky_wallets.csv')






