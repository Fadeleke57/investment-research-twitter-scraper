# Twitter Sentiment Analysis for Stocks

Scrapes Twitter for tweets about a given stock symbol, using Selenium WebDriver with Microsoft Edge, and performs sentiment analysis on the collected tweets using TextBlob. This can be useful for gauging public sentiment towards specific stocks or you can shift to your own use-case. (*The method and release of selenium for scraping in this program is now outdated and Twitter has recently used safegaurds against this scraping technique*).

### Features:
-Twitter scraping using Selenium WebDriver<br>
-Sentiment analysis of tweets with TextBlob<br>
-Support for Microsoft Edge browser via msedge.selenium_tools<br>
-Relays overall sentiment for a specificied stock symbol<br>

### Prerequisites:
Python3<br>
Microsoft Edge browser<br>
Microsoft Edge WebDriver (Has to match the browser version).

### Installation:
First, clone this repository to your local machine:
```
git clone https://github.com/Fadeleke57/investment-research-twitter-scraper.git
cd investment-research-twitter-scraper
```

Install the needed dependencies:
```
pip install -r requirements.txt
```

*Make sure you have the Microsoft Edge WebDriver installed and added to your system's PATH. Download it from the [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH) page, matching the version with your Edge browser.*
<br>
<br>

To run the program, use the command:

```
python main.py
```
