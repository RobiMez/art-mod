import os
from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler, Updater,
    DispatcherHandlerStop,
    Filters,
    MessageHandler,
    run_async
)

# ----------------------------------------------------------------
# Constants : basically a control panel to set the :
# bot token , log channel and admin group
TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20"
group_chat_id = '-1001158819991'
channel_id = '-1001326503520'
# ----------------------------------------------------------------
PORT = int(os.environ.get('PORT', '8443'))  # webhook things
updater = Updater(TOKEN)  # Updater declaration

print('\n----------- - ✔️  Bot is Alive - ----------\n')

# ----------------------------------------------------------------
# functionality


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Welcome dude \nSend /help if you are not sure what to do ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Send art here and i will send it to admins for them to verify and we will post it to the Emvc channel to get you some recognition kay .')


def artHandler(update, context):
    """handle art from the bot 
    take the art from the bot 
    send it to the admins group that is linked to the final channel 
    """

    message = update.effective_message
    file_id = message.photo[0].file_unique_id
    print("\n------------ artHandler message ----------\n")
    print(message)
    print("\n------------ artHandler file_id ----------\n")
    print(file_id)
    print("\n------------------------------------------\n")
    keyboard = InlineKeyboardMarkup([{
        InlineKeyboardButton(
            "Accept", callback_data=f"accept_art({file_id})")
    }, {
        InlineKeyboardButton(
            "Reject", callback_data=f"reject_art({file_id})")
    }])

    context.bot.send_photo(
        chat_id=group_chat_id,
        photo=message.photo[0].file_id,
        caption=f"""
Artist : {message.chat.first_name}
Username : {message.chat.username}
""",    parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard)


def accept_button(update, context):
    """handles the art accept button 
    """

    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    file_id = data['message']['photo'][0].file_id

    print("\n----------- accept_button message  ----------\n")
    print(message)
    print("\n----------- accept_button user_data ---------\n")
    print(user_data)
    print("\n----------- accept_button file_id  ----------\n")
    print(file_id)
    print("\n---------------------------------------------\n")
    context.bot.send_message(
        chat_id=user_data.id, text="your art has been accepted and is posted to the channel")
    context.bot.send_photo(chat_id=channel_id, photo=file_id, caption=f"""
Artist : {user_data.first_name} {user_data.last_name}
Username : @{user_data.username}
""")


def reject_button(update, context):
    """handles the art reject button 
    """

    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    file_id = data['message']['photo'][0].file_id

    print("\n----------- reject_art message  ----------\n")
    print(message)
    print("\n----------- reject_art user_data ---------\n")
    print(user_data)
    print("\n----------- reject_art file_id  ----------\n")
    print(file_id)
    print("\n---------------------------------------------\n")

    context.bot.send_message(
        chat_id=user_data.id, text="Sorry but your art has been rejected ")


# ----------------------------------------------------------------
# Dispatchers and Handlers go here
ACCEPT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    accept_button, pattern=r"accept_art")
REJECT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    reject_button, pattern=r"reject_art")

dp = updater.dispatcher  # Declaring the dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.photo, artHandler))
dp.add_handler(ACCEPT_CALLBACK_QUERY_HANDLER)
dp.add_handler(REJECT_CALLBACK_QUERY_HANDLER)

# ----------------------------------------------------------------
# Webhook stuff
# ⚠ DO NOT TOUCH !
# unless you know what you doing
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
