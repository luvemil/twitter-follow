import telegram
import logging
from tools import default_parse_status, format_status

def make_push_tweet(bot,author_id_str,targets,msg_q=None):
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
            try:
                bot.send_message(
                        chat_id=gid,
                        text=msg,
                        parse_mode=telegram.ParseMode.MARKDOWN
                        )
            except telegram.error.BadRequest:
                # TODO: Try resending BadRequests
                logging.info("BadRequest caught sending message: {}".format(msg))
            except telegram.error.TimedOut:
                # NOTE: When a TimeOut occurs, apparently the message gets sent anyway
                logging.info("TimeOut caught sending message: {}".format(msg))

    return push_tweet

