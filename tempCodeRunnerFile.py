driver.get('https://twitter.com/solucky__games/status/1522200777829367809')
wallets = driver.find_elements(by=By.TAG_NAME, value='article')
usernames = []

for w in wallets:
    tweet = w.find_elements(by=By.TAG_NAME, value='span')
    for t in tweet:
        if t.text.startswith('@'):
            usernames.append(t.text)
            
        

    usernames = set(usernames)
    usernames