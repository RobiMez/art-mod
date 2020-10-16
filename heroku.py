import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome dude')


dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
