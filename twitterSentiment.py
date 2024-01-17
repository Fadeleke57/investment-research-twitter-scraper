import pandas as pd
from textblob import TextBlob
import re
import Scraper


def load_data(filepath):  
    df = pd.read_csv(filepath) #loads tweet data from CSV file
    return df

def preprocess_data(df):
    df['CleanTweet'] = df['TweetText'].apply(clean_tweet) #Preprocess the data for sentiment analysis.
    return df

def clean_tweet(tweet):
    tweet = tweet.lower()  #letters to lowercase 
    #the rest of this cleans out junk in the tweet that doesn't need to be proccessed
    tweet = re.sub('http\S+\s*', '', tweet)  #urls
    tweet = re.sub('RT|cc', '', tweet)  #rt and cc
    tweet = re.sub('#\S+', '', tweet)  #hashtags
    tweet = re.sub('@\S+', '', tweet)  #mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  #punctuations
    tweet = re.sub('\s+', ' ', tweet)  # removes extra whitespace
    return tweet

#uses textBlobs text proccessing for analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

#applies sentiment anlysis
def apply_sentiment_analysis(df):
    df['Sentiment'] = df['CleanTweet'].apply(analyze_sentiment)
    return df

#takes the mean of scores to get an overall
def aggregate_results(df):
    average_sentiment = df['Sentiment'].mean()
    return average_sentiment

#displays results
def interpret_results(score):
    """Interpret the overall sentiment score."""
    if score > 0:
        return "Positive Sentiment"
    elif score < 0:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"

def perform_sentiment_analysis(csv_path): #function that uses helper functions to druve analysis
    df = load_data(csv_path)
    df = preprocess_data(df)
    df = apply_sentiment_analysis(df)
    score = aggregate_results(df)
    result = interpret_results(score)
    return result

#batta bing batta boom    
def main():
    stock_index = input("Enter the stock index (e.g., NASDAQ): ")
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")
    
    # starts scraping from Scraper.py
    csv_path = Scraper.scrape(stock_index, stock_symbol)

    # performs sentiment analysis
    sentiment = perform_sentiment_analysis(csv_path)
    print("Overall Sentiment for " +  str(stock_symbol) + " : " + str(sentiment))

if __name__ == "__main__":
     main()