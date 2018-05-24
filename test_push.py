import tweepy

from setup import auth,setup_api
from handlers import *
from tbot import bot, updater, groups
from tools import *
import telegram
import pickle
import codecs

import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

api = setup_api(auth)

sender_id = '52424550' # Il fatto quotidiano

msgs = []

def push_tweet(status):
    if status.author.id == sender_id:
        p_status = default_parse_status(status)
        msg = "*{} @ {}*: {}".format(
                p_status['author'],
                p_status['date'],
                p_status['content']
                )
    else:
        msg = format_status(status)

    msgs.append(msg)
    for gid in groups:
        try:
            bot.send_message(
                    chat_id=gid,
                    text=msg,
                    parse_mode=telegram.ParseMode.MARKDOWN
                    )
        except telegram.error.BadRequest:
            logging.info("Error sending message: {}".format(msg))

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
    print("Writing tweets to file")
    outfile = codecs.open("tweets","a","utf-8")
    for msg in msgs:
        outfile.write(msg+"\n")
    outfile.close()
    print("Tweets, written")
    print("Stream closed. Goodbye!")
