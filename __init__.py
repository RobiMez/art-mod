# import logging

# from telegram import ChatPhoto
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)


# logger = logging.getLogger(__name__)


# # Define a few command handlers. These usually take the two arguments update and
# # context. Error handlers also receive the raised TelegramError object in error.
# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('Welcome dude')


# def help_command(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('What do you need asisctance with ')


# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)
#     print("\n------------------------------------")
#     print(update.message)
#     print("------------------------------------\n")


# def addart(update, context):
#     """Echo the user picture. with a desc """
#     print("\n------------------------------------")
#     print(update)
#     print("------------------------------------\n")
#     update.message.reply_text("now send me your art:")


# photoid = 'AgACAgQAAxkBAAM4X4gtKynlDSPcfUU8lndi-PxlEmIAAh20MRsa7UlQjoJoG94IKeUX1qknXQADAQADAgADbQADwkMBAAEbBA'


# def handlephotos(update, context):
#     """ handles the incoming pic """
#     message = update.effective_message
#     print("\n--------------- ß ---------------")
#     print(update)
#     print("----------------- ß -----------------\n")
#     print(message)
#     print("------------------------------------\n")
#     message.reply_photo(photoid, caption=f"""
# Artist : {message.chat.first_name}
# Username : {message.chat.username}
#                         """)


# def caps(update, context):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id='-1001487552790', text=text_caps)


# caps_handler = CommandHandler('caps', caps)


# def main():
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     # Make sure to set use_context=True to use the new context based callbacks
#     # Post version 12 this will no longer be necessary
#     updater = Updater(
#         "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20", use_context=True)

#     # Get the dispatcher to register handlers
#     dp = updater.dispatcher

#     # on different commands - answer in Telegram
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("help", help_command))
#     dp.add_handler(CommandHandler("addart", addart))
#     dp.add_handler(caps_handler)
#     # handle photos
#     dp.add_handler(MessageHandler(Filters.photo, handlephotos))
#     # # handle photos
#     # dp.add_handler(MessageHandler(Filters.photo, handleaddart))
#     # # handle photos
#     # dp.add_handler(MessageHandler(Filters.photo, handleaddart))

#     # on noncommand i.e message - echo the message on Telegram
#     # dp.add_handler(MessageHandler(Filters.all & ~Filters.command, echo))

#     # Start the Bot
#     updater.start_polling()

#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()


# if __name__ == '__main__':
#     main()
