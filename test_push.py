import tweepy

from setup import auth,setup_api
from handlers import *
from tbot import bot, updater, groups
from tools import *
import telegram
import pickle
import codecs
from callbacks import *
from debugger import debugger

# Setup debugging
debugger.set_debugging()

import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

api = setup_api(auth)

sender_id = '52424550' # Il fatto quotidiano

msgs = []

push_tweet = make_push_tweet(bot,sender_id,groups,msgs)
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
    debugger.save("bad_tweets","bad_tweets.pickle")
    print("Tweets, written")
    print("Stream closed. Goodbye!")
