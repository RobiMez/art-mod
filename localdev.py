import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          DispatcherHandlerStop, Filters, MessageHandler,
                          run_async)
TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20"
# PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

group_chat_id = '-1001158819991'
channel_id = '-1001326503520'


print('\n----------- - ✔️  Bot Alive - ----------\n')
# add handlers


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Welcome dude \nSend /help if you are not sure what to do ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Send art here and i will send it to admins for them to verify and we will post it to the Emvc channel to get you some recognition kay .')


def do_sth(id):
    print(id)


def artHandler(update, context):
    """handle art from the bot 
    take the art from the bot 
    send it to the admins group that is linked to the final channel 
    """

    message = update.effective_message
    print(message)
    file_id = message.photo[0].file_unique_id
    print(file_id)
    keyboard = InlineKeyboardMarkup([{
        InlineKeyboardButton(
            "verify art ", callback_data=f"verify_art({file_id})")
    }])

    context.bot.send_photo(chat_id=group_chat_id, photo=message.photo[0].file_id, caption=f"""
--- Bot generated verification message ---
Artist : {message.chat.first_name}
Username : {message.chat.username}
""", parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)


def verify_button(update, context):
    """handles the verification process

    """

    message = update.effective_message
    data = update.callback_query
    file_id = data['message']['photo'][0].file_id
    print("----------------------")
    print(message)
    print("----------------------")
    print(data)
    print("----------------------")
    print(file_id)
    print("----------------------")

    context.bot.send_photo(chat_id=channel_id, photo=file_id, caption=f"""
--- verified to channel  ---
Artist : {message.chat.first_name}
Username : {message.chat.username}
Description : lorem ipsum sir dolor amet
""")

# https://t.me/Emvc_group

# https://t.me/emvc_channel


# @EMVC_test_bot
CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    verify_button, pattern=r"verify_art")

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CALLBACK_QUERY_HANDLER)
dp.add_handler(CommandHandler("help", help))
# dp.MessageHandler(Filters.chat(-1234), callback_method)
dp.add_handler(MessageHandler(Filters.photo, artHandler))

# ----------------------------------------------------------------
# webhook shit
# do not touch
# unless you know what you doing
# updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.start_polling()
# updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
