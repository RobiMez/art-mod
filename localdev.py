import os
import re
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
# old test bot 
# TOKEN = "1086396783:AAFl7mW9mkuYnmwenRePOW-RSR2AOzurC20" 
TOKEN = "1394105957:AAEyrPr8p0ikqKPbyUs54wxZSlo-wsaXeoA"
group_chat_id = '-1001158819991'
channel_id = '-1001326503520'
# ----------------------------------------------------------------
PORT = int(os.environ.get('PORT', '8443'))  # webhook things
updater = Updater(TOKEN)  # Updater declaration

print('\n----------- - ✔️  Bot is Alive - ----------\n')
# reuben , meareg , michael ,sterling archer (R)
admins_id_list = [567142057, 356768912, 172497135, 370227928, 979190369]

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


def albumhandler(update, context):
    """handle album art from the bot
triggered by /album
"""
    update.message.reply_text(
        'Start sending me your art and send /album_done when finished ')


def albumdonehandler(update, context):
    """handle album art from the bot
triggered by /album
"""
    update.message.reply_text(
        'kay .. what now  ')


def artHandler(update, context):
    """handle art from the bot
    take the art from the bot
    send it to the admins group that is linked to the final channel
    """

    message = update.effective_message
    isgroup = message.media_group_id
    user_data = message.from_user
    caption = message.caption
    file_id = message.photo[0].file_unique_id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    name = ''
    username = message.chat.username
    if first_name:
        name = name + first_name
        if last_name:
            name = name + ' ' + last_name

    print(f"""
    ----------------- Art handler logs -----------------
    --------  message  ---------

    {message}
    --------  name  ---------

    {name}
    ---------  user_data  --------

    {user_data}
    -------  file_id  ----------

    {file_id}
    --------  caption  ---------

    {caption}
    -----------------
        """)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Accept", callback_data=f"accept_art({user_data.id})"), InlineKeyboardButton(
            "Reject", callback_data=f"reject_art({user_data.id})")],
    ])
    if isgroup:
        print('This message is an album ignoring')
        context.bot.send_message(
            chat_id=user_data.id, text="loooks like you are trying to send an album ... please use /album for that ")
    else:
        context.bot.send_photo(
            chat_id=group_chat_id,
            photo=message.photo[0].file_id,
            caption=f"""
    {name} @{username}

    Description  :
    {caption}
    """,

            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard)

        context.bot.send_message(
            chat_id=user_data.id, text="I have sent your art to the admins for moderation , hang tight . ")


def accept_button(update, context):
    """handles the art accept button
    """

    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    caption = message.caption
    query = update.callback_query
    file_id = data['message']['photo'][0].file_id
    # admins = context.bot.get_chat_administrators(group_chat_id)
    # for admin in admins:
    #     admins_id_list.append(admin.user.id)
    # print(admins_id_list)
    original_author = re.match(r"accept_art\((.+?)\)", query.data)
    original_author_str = original_author.group()
    original_author_id = re.findall(r"\d", original_author_str)
    original_author_id_int = ""
    for x in original_author_id:
        original_author_id_int = original_author_id_int + x
    orig_author_id = int(original_author_id_int)
    # original_author_id = re.match("[0123456789]", original_author.group())
    print("\n----------- accept_button message  ----------\n")
    print(message)
    print("\n----------- accept_button user_data ---------\n")
    print(user_data)
    print("\n----------- accept_button file_id  ----------\n")
    print(file_id)
    print("\n----------- accept_button caption -----------\n")
    print(caption)
    print("\n----------- accept_button admins ------------\n")
    # print(admins[0])
    print("\n-------- accept_button original_author ------\n")
    print(original_author)
    print("\n-------- accept_button original_author_id ------\n")
    print(original_author_id)
    print(int(original_author_id_int))
    # print(type(original_author.group()))

    print("\n---------------------------------------------\n")
    # adminstrator check
    if user_data.id in admins_id_list:

        print("all good , this guy is an admin ")

        context.bot.send_message(
            chat_id=orig_author_id,
            text="Congrats your art has been accepted and posted to the EMVC channel")
        context.bot.delete_message(
            chat_id=group_chat_id,
            message_id=message.message_id)
        context.bot.send_photo(
            chat_id=channel_id,
            photo=file_id,
            caption=f"""
    {caption}
    """)
    else:
        print("Non admin trying to accept art , ignoring  ")


def reject_button(update, context):
    """handles the art reject button
    """

    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    query = update.callback_query
    file_id = data['message']['photo'][0].file_id

    original_author = re.match(r"reject_art\((.+?)\)", query.data)
    original_author_str = original_author.group()
    original_author_id = re.findall(r"\d", original_author_str)
    original_author_id_int = ""
    for x in original_author_id:
        original_author_id_int = original_author_id_int + x

    orig_author_id = int(original_author_id_int)

    print("\n----------- reject_art message  ----------\n")
    print(message)
    print("\n----------- reject_art user_data ---------\n")
    print(user_data)
    print("\n----------- reject_art file_id  ----------\n")
    print(file_id)
    print("\n---------------------------------------------\n")

    if user_data.id in admins_id_list:
        print("all good , this guy is an admin ")
        context.bot.send_message(
            chat_id=orig_author_id, text="Sorry your art has been rejected, possible reasons can be breaking the rules, check @EMVC_Rules")
        context.bot.delete_message(
            chat_id=group_chat_id, message_id=message.message_id)
    else:
        print("Non admin trying to reject art , ignoring  ")


# ----------------------------------------------------------------
# Dispatchers and Handlers go here
ACCEPT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    accept_button, pattern=r"accept_art")
REJECT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    reject_button, pattern=r"reject_art")

dp = updater.dispatcher  # Declaring the dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("album", albumhandler))
dp.add_handler(CommandHandler("album_done", albumdonehandler))
dp.add_handler(MessageHandler(Filters.photo, artHandler))
dp.add_handler(ACCEPT_CALLBACK_QUERY_HANDLER)
dp.add_handler(REJECT_CALLBACK_QUERY_HANDLER)
# ----------------------------------------------------------------
# webhook shit
# ⚠ DO NOT TOUCH !
# unless you know what you doing

# updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.start_polling()
# updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
