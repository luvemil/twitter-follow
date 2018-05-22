
def _get_user_timeline(api,id,count=10):
# Not really useful
    return api.user_timeline(id=id,count=count)[::-1]

def format_status(status):
    author_name = status.author.screen_name
    content = status.text
    date = status.created_at.strftime("%Y-%m-%d %H:%M:%S")
    return "{} @ {}: {}".format(author_name,date,content)
