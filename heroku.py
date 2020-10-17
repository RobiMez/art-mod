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
        'Hey There bud , Im the EMVC bot \n send me your art so that i can post them to the EMVC channel \n send /help for how to use me ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Send me your art here and i will send it to the admins for them to verify\n and then we will post it to the Emvc channel to get you some recognition, adding the description function soon.')


def todo(update, context):
    """Send a message when the command /todo is issued."""
    update.message.reply_text(
        """ 
Features to add will be 
- The Description should be user input
- The user link should have "@" in-front of it.
- We also have an art category, I'd like u to test out a button way of posting the art category. I.e, when the art is posted on the channel below the description there should be an art category that are hardcoded hashtags like #environment, #character, #vfx and so on.
So the flow of input should be more like.

User sends Art -> Bot asks what the description of the art is -> User types the description of the art -> Bot gives a list of buttons to pick the type of art posted -> Bot sends a message that the art is sent to the admins waiting for approval.


Bot reaches to admin group and posts the art with the users link so we can contact him to make changes , there should be an accept and reject option. A rejection will send the user that his art is rejected. The accept button will do what it does now to the channel, with the added features mentioned above. 

The rest is absolutely perfect.""")


def artHandler(update, context):
    """desc 
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
    """Handles the verification process
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
Artist : {message.chat.first_name}
Username : {message.chat.username}
Description : lorem ipsum sir dolor amet
Tags : 
""")


# ----------------------------------------------------------------
# Dispatchers and Handlers go here
CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    verify_button, pattern=r"verify_art")

dp = updater.dispatcher  # Declaring the dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("todo", todo))
dp.add_handler(MessageHandler(Filters.photo, artHandler))
dp.add_handler(CALLBACK_QUERY_HANDLER)


# ----------------------------------------------------------------
# Webhook stuff
# ⚠ DO NOT TOUCH !
# unless you know what you doing
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
