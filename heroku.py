import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

print('\n----------- - Bot Alive - ----------\n')
# add handlers


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Welcome dude \nSend /help if you are not sure what to do ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Send art here and i will send it to admins for them to verify and we will post it to the Emvc channel to get you some recognition kay .')


photoid = 'AgACAgQAAxkBAAM4X4gtKynlDSPcfUU8lndi-PxlEmIAAh20MRsa7UlQjoJoG94IKeUX1qknXQADAQADAgADbQADwkMBAAEbBA'


def artHandler(update, context):
    """Send a message when the command /help is issued."""
    message = update.effective_message
    context.bot.send_message("check this guy ")
    context.bot.send_photo(chat_id='-1001487552790', photoid, caption=f"""
Artist : {message.chat.first_name}
Username : {message.chat.username}
                        """)


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
