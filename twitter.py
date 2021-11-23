import tweepy
import time
import itertools
from os import environ 


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

numberOfTweets = 100

accountsToFollow = ['CryptoBurstGame','Crypto_Shooter','SparkDeFi','CryptoSlicer','sparkpointio']

for user_name in itertools.cycle(accountsToFollow):
    user = api.get_user(screen_name = user_name)
    print(user.screen_name)

    for tweet in tweepy.Cursor(api.user_timeline, id=user.screen_name).items(numberOfTweets):
        try:
            if not tweet.retweeted:
                tweet.favorite()
                print('Tweet Liked!')
                tweet.retweet()
                print('Tweet Retweeted!')
                time.sleep(3600)
                break

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break