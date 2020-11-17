import tweepy
import time

auth = tweepy.OAuthHandler('4ioe3QSWFx0O0Ch1ULpRw8oiU','d922ZaD2oElJrU1rC9VNiwqCjo6kBtALxgXQbUDn074E0ZCgDz')

auth.set_access_token('968706030061441027-EYePu0fNJSqgNJaiDjsX2kKh0UAEg4j','g5cCTWCfzYbMf6jE0TmeSj4UdBgp2UOgXEdjSe9xzsGv4')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user.screen_name)

sparkPoint = api.get_user("JRNYcrypto")

# print("User details:")
# print(sparkPoint.name)
# print(sparkPoint.description)
# print(sparkPoint.location)

# print("Last 20 Followers:")
# for follower in sparkPoint.followers():
#     print(follower.name)


timeline = sparkPoint.timeline()

for tweet in timeline:
    # print(f"{tweet.user.name} said {tweet.text}")
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

# api.update_status("Yeah, I saw it bellow, so its working...")
# for follower in tweepy.Cursor(api.followers).items():
# 	print(follower.name)

# Likes the tweet
# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)