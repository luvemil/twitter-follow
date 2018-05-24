import tweepy
from tools import format_status
import logging

def null_fun(*args, **kwargs):
    return

class MyStreamListener(tweepy.StreamListener):
    def __init__(self,callback=null_fun):
        super(MyStreamListener,self).__init__()
        self.callback = callback

    def on_status(self, status):
        status_s = format_status(status)
        logging.debug(status_s)
        self.callback(status_s)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class CallbackStreamListener(tweepy.StreamListener):
    def __init__(self,callback=null_fun):
        super(CallbackStreamListener,self).__init__()
        self.callback = callback

    def on_status(self, status):
        self.callback(status)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

