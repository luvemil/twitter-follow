import tweepy

from setup import auth,setup_api
from handlers import *
from tbot import bot, updater, groups
from tools import format_status

import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

api = setup_api(auth)

sender_id = '52424550' # Il fatto quotidiano

def push_tweet(status):
    if status.author.id == sender_id:
        msg = "! " + format_status(status)
    else:
        msg = format_status(status)
    for gid in groups:
        bot.send_message(chat_id=gid,text=msg)

myStreamListener = CallbackStreamListener(callback=push_tweet)
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

try:
    updater.start_polling()
    myStream.filter(follow=[sender_id])
except KeyboardInterrupt:
    print("Received interrupt, shutting down...")
finally:
    updater.stop()
    myStream.disconnect()
    print("Stream closed. Goodbye!")
