import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

print('----------- - Bot Alive - ----------')
# add handlers


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Welcome dude \nsend /help if you are not sure what to do ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'send art here and ill send it to admins for them to verify and we will post it to the emvc channel to get you some recognition kay .')


dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))


# ----------------------------------------------------------------
# webhook shit
# do not touch
# unless you know what you doing
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
