#Prompts the user to enter the stock they wish to inquire about

stock_exchange = str(input("Enter a stock exchange(i.e. NASDAQ): "))
stock_symbol = str(input("Enter the corresponding stock symbol or ticker(i.e. APPL): "))

#functions that help gain access to web browser as well as a sleep attribute to allow time for the page to load first

import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#naviagtes to twitter

driver.get('https://www.twitter.com/login')

sleep(3)

#enters username

username = driver.find_element_by_xpath('//input[@name="text"]') 
username.send_keys('FaroukAdeleke3')

next_button = driver.find_element_by_xpath("//span[contains(text(), 'Next')]")
next_button.click()

sleep(3)

#enters password and logs in

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('Fadeleke57')
log_in = driver.find_element_by_xpath("//span[contains(text(), 'Log in')]")
log_in.click()
driver.maximize_window()

sleep(6)

#enters and returns previously asked information into twitter search bar

search_bar = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_bar.send_keys(stock_exchange + ": "+ stock_symbol)
search_bar.send_keys(Keys.RETURN)

#latest tab

sleep(5)
latest_button = driver.find_element_by_xpath("//span[contains(text(), 'Latest')]")
latest_button.click()

cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

card = cards[0]

#collect username

card.find_element_by_xpath('.//span').text

card.find_element_by_xpath('.//span[contains(text(), "@")]').text

card.find_element_by_xpath('.//time').get_attribute('datetime')

comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
full_tweet = comment + responding

def get_tweet_data(card):
    '''Gets datat from tweet'''
    username = card.find_element_by_xpath('.//span').text
    handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    full_tweet = comment + responding

    tweet = (username, handle, postdate, full_tweet)

get_tweet_data(card)

tweet_data = []

for card in cards:
    data = get_tweet_data(card)
    if data:
        tweet_data.append(data)

tweet_data[0]

driver.execute_script



