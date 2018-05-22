import tweepy

from setup import auth,setup_api
from handlers import MyStreamListener
from tbot import bot, updater, groups

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

api = setup_api(auth)

def push_tweet(msg):
    for gid in groups:
        bot.send_message(chat_id=gid,text=msg)

myStreamListener = MyStreamListener(callback=push_tweet)
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

try:
    updater.start_polling()
    myStream.filter(track=['juventus'])
except KeyboardInterrupt:
    print("Received interrupt, shutting down...")
finally:
    updater.stop()
    myStream.disconnect()
    print("Stream closed. Goodbye!")
