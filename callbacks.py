import telegram
import logging
from tools import default_parse_status, format_status
import time
from debugger import record

def send_with_retry(bot,chat_id,msg,trynum=1,maxretry=5):
    try:
        bot.send_message(
                chat_id=chat_id,
                text=msg,
                parse_mode=telegram.ParseMode.MARKDOWN
                )
    except telegram.error.BadRequest:
        # TODO: Try resending BadRequests
        logging.info("BadRequest caught at try {} sending message: {}".format(trynum,msg))
        if trynum < maxretry:
            time.sleep(2)
            send_with_retry(bot,chat_id,msg,trynum+1,maxretry)
        else:
            logging.info("BadRequest exceeds maxretry for message: {}".format(msg))
            record(bad_tweets=msg)
    except telegram.error.TimedOut:
        # NOTE: When a TimeOut occurs, apparently the message gets sent anyway
        logging.info("TimeOut caught sending message: {}".format(msg))

def make_push_tweet(bot,author_id_str,targets,msg_q=None,bad_request_retries=1):
    sender_id = str(author_id_str)

    def push_tweet(status):
        p_status = default_parse_status(status)
        if status.author.id_str == sender_id:
            msg = "*{} @ {}*:\n{}".format(
                    p_status['author'],
                    p_status['date'],
                    p_status['content']
                    )
        else:
            msg = "-- {} @ {}:\n{}".format(
                    p_status['author'],
                    p_status['date'],
                    p_status['content']
                    )

        if msg_q is not None:
            msg_q.append(msg)
        for gid in targets:
            send_with_retry(bot,gid,msg,bad_request_retries)

    return push_tweet

