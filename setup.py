import pickle
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

from tweepy.auth import OAuthHandler

import os
auth = OAuthHandler(os.getenv("CONSUMER_KEY"),os.getenv("CONSUMER_SECRET"))
# auth.set_access_token(os.getenv("ACCESS_TOKEN"),os.getenv("ACCESS_TOKEN_SECRET"))

import tweepy
api = tweepy.API(auth)

def get_api_token(auth):
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
        return None

    print("Visit {} and write here the code".format(redirect_url))
    verifier = input('Verifier:')

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')

    access_data = {
            "key": auth.access_token,
            "secret": auth.access_token_secret,
            "status": "OK"
            }
    token_file = open("token.pickle","wb")
    pickle.dump(access_data,token_file)
    token_file.close()
    return auth

def setup_api(auth):
    try:
        token_file = open("token.pickle","rb")
        access_data = pickle.load(token_file)
        token_file.close()
        if access_data["status"] != "OK":
            raise ValueError("Status is not OK")
        auth.set_access_token(access_data["key"],access_data["secret"])
    except ValueError:
        token_file.close()
        auth = get_api_token(auth)
    except FileNotFoundError:
        auth = get_api_token(auth)

    api = tweepy.API(auth)
    return api
