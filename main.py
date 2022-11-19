from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from selenium import webdriver
import time
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
sleep(3)
message ='Watsup!'
messages = [
  'Gm',
  'nice one!',
  'Gm ❤️',
  'fresh!',
  'Gm 👽',
  'Wadupp',
  'sweet',
  'lets go!',
  'its good day!',
  'love it!',
]

while True:
  try:
    driver.refresh()
    sleep(5)
    tweets = driver.find_elements(by=By.TAG_NAME, value='article')
    print('hi')
    tweet = tweets[1]
    svgs = tweet.find_elements(by=By.TAG_NAME, value='svg')
    svgs[3].click()#like
    svgs[1].click()
    sleep(5)
    reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
    i = randint(0, len(messages)-1)
    print(i,messages[i])
    reply_in.send_keys (messages[i])
    reply_in.send_keys(Keys.ENTER)
    reply = driver.find_elements(by=By.TAG_NAME, value='span')
    for r in reply:
      if r.text == 'Reply':
        r.click()
        break
      elif r.text == 'Unsent Tweet':
        break
    sleep(8)
  except:
    sleep(2)
    driver.get('https://www.twitter.com/home')
    continue







# tweets = driver.find_elements(by=By.TAG_NAME, value='article')

# for tweet in tweets:
#   mess = tweet.find_elements(by=By.TAG_NAME, value='span')[4].text
#   if mess == 'See more':
#     mess = tweet.find_elements(by=By.TAG_NAME, value='span')[6].text
#   print(mess)


# tweet.click()

# for tweet in tweets:

#   try: 
#     svgs = tweet.find_elements(by=By.TAG_NAME, value='svg')
#     svgs[1].click()#like
#     svgs[5].click()
#   except:
#     svg
#   tweet.find_elements(by=By.TAG_NAME, value='svg')[3].click() # like click
#   sleep(1)
#   tweet.find_elements(by=By.TAG_NAME, value='svg')[1].click() # comment click
#   sleep(1)
#   reply_in = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
#   i = randint(0, len(messages)-1)
#   reply_in.send_keys (messages[i])
#   reply = driver.find_elements(by=By.TAG_NAME, value='span')
#   for r in reply:
#     if r.text == 'Reply':
#       r.click()
#       break
#   sleep(1)
