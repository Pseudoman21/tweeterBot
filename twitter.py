import tweepy
import time

auth = tweepy.OAuthHandler('4ioe3QSWFx0O0Ch1ULpRw8oiU','d922ZaD2oElJrU1rC9VNiwqCjo6kBtALxgXQbUDn074E0ZCgDz')

auth.set_access_token('968706030061441027-EYePu0fNJSqgNJaiDjsX2kKh0UAEg4j','g5cCTWCfzYbMf6jE0TmeSj4UdBgp2UOgXEdjSe9xzsGv4')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

sparkPoint = api.get_user("Crypto_Shooter")

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

