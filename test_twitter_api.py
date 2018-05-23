import tweepy

from setup import auth,setup_api
from handlers import MyStreamListener

import os

target_id = os.getenv("DEFAULT_TWITTER_TARGET")

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

api = setup_api(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

try:
    myStream.filter(track=['juventus'])
except KeyboardInterrupt:
    print("Received interrupt, shutting down...")
finally:
    myStream.disconnect()
    print("Stream closed. Goodbye!")
