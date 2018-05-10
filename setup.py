from dotenv import load_dotenv
load_dotenv()

from tweepy import OAuthHandler

import os
auth = OAuthHandler(os.getenv("CONSUMER_KEY"),os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"),os.getenv("ACCESS_TOKEN_SECRET"))

import tweepy
api = tweepy.API(auth)
