from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)

def get_tweets(card):
  try:
    posttime = card.find_element('xpath', './/time').get_attribute('datetime')
  except NoSuchElementException:
    return
  if card:
    tweet = card.find_element('xpath', './/div[@data-testid="tweetText"]').text
  return tweet

search = input('enter search query: ')
search = search.replace(' ', '%20')
datef= input('Enter date from:(YYYY-MM-DD) ')
datet= input('Enter date to:(YYYY-MM-DD) ')
url = 'https://twitter.com/search?q="' + search + '"%20until%3A' + datet + '%20since%3A' + datef + '&src=typed_query&f=top'

driver.get(url)
sleep(3)

tweets = []
tweet_ids = set()
last_pos = driver.execute_script("return window.pageYOffset;")
scrolling = True

while scrolling:
  cards = driver.find_elements('xpath','//article[@data-testid="tweet"]')
  sleep(2)
  if len(cards)!=0:
    for card in cards:
      data = get_tweets(card)
      if data:
        tweet_id = ''.join(data)
        if tweet_ids not in tweet_ids:
          tweet_ids.add(tweet_id)
          tweets.append(data)
  scroll_attempt = 0
  while True:
      driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
      sleep(2)
      curr_position = driver.execute_script("return window.pageYOffset;")
      if last_pos == curr_position:
          scroll_attempt += 1
          if scroll_attempt >= 3:
              scrolling = False
              break
          else:
              sleep(2)
      else:
          last_pos = curr_position
          break

print("Number of tweets found: ", len(tweets))
print("Top tweets: ")
if len(tweets)<10:
  for  tweet in tweets:
    print(tweet)
else:
  for i in range(10):
    print(tweets[i])
