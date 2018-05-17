import tweepy

from setup import auth,setup_api
from handlers import MyStreamListener

api = setup_api(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['juventus'])
