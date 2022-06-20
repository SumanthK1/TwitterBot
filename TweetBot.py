import tweepy
import configparser
import pandas as pd

# Reading the configurations file for the required values
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Allowing authentication to Twitter account
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Setting Tweepy API
api = tweepy.API(auth)

# Getting public tweets from timeline
public_tweets = api.home_timeline()

# Creating and organizing DataFrame
columns = ['TIME', 'USER', 'TWEET']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

# Setting up and creating CSV file for DataFrame
dataFrame = pd.DataFrame(data, columns=columns)
dataFrame.to_csv('timelineTweets.csv')
