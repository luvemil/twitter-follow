import telegram
from telegram.ext import Updater, CommandHandler
import os

debug_flag = os.getenv("DEBUG")

import logging

# Ensure dotenv was loaded
bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
updater = Updater(bot=bot)

groups = []
def register_group(bot,update):
    try:
        gid = update.message.chat.id
        if gid in groups:
            update.message.reply_text("Already registered")
        else:
            groups.append(update.message.chat.id)
            update.message.reply_text("You have been registered and will receive updates")
        logging.debug("groups listing START")
        for gid in groups:
            logging.debug("-- {}".format(gid))
        logging.debug("groups listing END")
    except:
        update.message.reply_text("Something went wrong")

def delete_group(bot,update):
    try:
        gid = update.message.chat.id
        if gid in groups:
            groups.remove(gid)
    except:
        logging.debug("Error removing group from list")

def debug_echo_groups(bot,update):
    logging.debug("len(groups): {}".format(len(groups)))
    if len(groups) > 0:
        update.message.reply_text(' '.join(map(str,groups)))
    else:
        update.message.reply_text("groups is empty")

updater.dispatcher.add_handler(CommandHandler('register',register_group))

if debug_flag == "true":
    updater.dispatcher.add_handler(CommandHandler('debug_echo_groups',debug_echo_groups))