import tweepy

from setup import auth,setup_api
from handlers import CallbackStreamListener
from tbot import bot, updater, groups
from callbacks import make_push_tweet

import os

target_id = os.getenv("DEFAULT_TWITTER_TARGET")

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

api = setup_api(auth)

push_tweet = make_push_tweet(bot,target_id,groups)

myStreamListener = CallbackStreamListener(callback=push_tweet)
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

try:
    updater.start_polling()
    myStream.filter(follow=[target_id])
except KeyboardInterrupt:
    print("Received interrupt, shutting down...")
finally:
    updater.stop()
    myStream.disconnect()
    print("Stream closed. Goodbye!")
