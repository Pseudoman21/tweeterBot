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

Crypto_Shooter = api.get_user("Crypto_Shooter")
CryptoBurstGame = api.get_user("CryptoBurstGame")
CryptoSlicer = api.get_user("CryptoSlicer")

sparkPoint = api.get_user("sparkpointio")

timeline = sparkPoint.timeline()

for tweetSparkIo in timeline:
    if not tweetSparkIo.favorited:
    	try:
    		api.create_favorite(tweetSparkIo.id)
    	except Exception as e:
    		logger.error("Error on fav", exc_info=True)
    if not tweetSparkIo.retweeted:
    	try:
    		tweetSparkIo.retweet()
    	except Exception as e:
    		logger.error("Error on fav and retweeted", exc_info=True)

for tweetShooter in timeline:
    if not tweetShooter.favorited:
        try:
            api.create_favorite(tweetShooter.id)
        except Exception as e:
            logger.error("Error on fav", exc_info=True)
    if not tweetShooter.retweeted:
        try:
            tweetShooter.retweet()
        except Exception as e:
            logger.error("Error on fav and retweeted", exc_info=True)

for tweetBurst in timeline:
    if not tweetBurst.favorited:
        try:
            api.create_favorite(tweetBurst.id)
        except Exception as e:
            logger.error("Error on fav", exc_info=True)
    if not tweetBurst.retweeted:
        try:
            tweetBurst.retweet()
        except Exception as e:
            logger.error("Error on fav and retweeted", exc_info=True)

for tweetSlicer in timeline:
    if not tweetSlicer.favorited:
        try:
            api.create_favorite(tweetSlicer.id)
        except Exception as e:
            logger.error("Error on fav", exc_info=True)
    if not tweetSlicer.retweeted:
        try:
            tweetSlicer.retweet()
        except Exception as e:
            logger.error("Error on fav and retweeted", exc_info=True)


