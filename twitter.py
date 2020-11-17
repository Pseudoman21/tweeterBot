import tweepy
import time
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

sparkPoint = api.get_user("Lakers")

timeline = sparkPoint.timeline()

for tweet in timeline:
    if not tweet.favorited:
    	try:
    		api.create_favorite(tweet.id)
    	except Exception as e:
    		logger.error("Error on fav", exc_info=True)
    if not tweet.retweeted:
    	try:
    		tweet.retweet()
    	except Exception as e:
    		logger.error("Error on fav and retweeted", exc_info=True)

