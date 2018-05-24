import tweepy

def _get_user_timeline(api,id,count=10):
# Not really useful
    return api.user_timeline(id=id,count=count)[::-1]

def get_replies_to_user(api,user_handle,since_id=None):
    search_q = "@{}".format(user_handle)
    return tweepy.Cursor(api.search,q=search_q,since_id=since_id)

def format_status(status):
    author_name = status.author.screen_name
    content = status.text
    date = status.created_at.strftime("%Y-%m-%d %H:%M:%S")
    return "{} @ {}: {}".format(author_name,date,content)
