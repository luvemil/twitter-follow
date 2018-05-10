import tweepy

from setup import auth,api
from handlers import MyStreamListener

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['juventus'])
