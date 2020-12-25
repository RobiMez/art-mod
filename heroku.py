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
# Bot token, Log channel and Admin group

TOKEN = "1394105957:AAEyrPr8p0ikqKPbyUs54wxZSlo-wsaXeoA"

admin_group_id = '-1001158819991'
comment_group_id = '-1001480804050'
art_channel_id = '-1001326503520'

# ----------------------------------------------------------------
# Webhook Configuration
PORT = int(os.environ.get('PORT', '8443'))
# Updater declaration
updater = Updater(TOKEN)
# reuben , meareg , michael ,sterling archer (R)
admins_id_list = [567142057, 356768912, 172497135, 370227928, 979190369]

# ---------------------------------------------------------------
print('\n⌛️  Bot is Waking up\n')
# Functionality 


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Welcome dude \nSend /help if you are not sure what to do ')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Send art here and i will send it to admins for them to verify and we will post it to the Emvc channel to get you some recognition kay .')


def photoHandler(update, context):
    """handle photo from the bot : 
    Photo art input from the bot 
    send to admin group for moderation 
    send to the channel if approved 
    
    """

    
    # Constants 
    # message : the message sent to the bot 
    message = update.effective_message
    # userdata : the user id and stuff from the bot 
    user_data = message.from_user
    # caption : the message caption of the message sent to the bot 
    # break here if not a pm 
    if message.chat['type'] == 'private':
        print("is a pm ")
        caption = message.caption
        # file id : the unique id of the image sent to the bot 
        file_id = message.photo[0].file_unique_id
        
        first_name = message.chat.first_name

        last_name = message.chat.last_name
        name = ''
        username = message.chat.username
        if first_name:
            name = name + first_name
            if last_name:
                name = name + ' ' + last_name

    # DEBUG ---------------------------------------------------------
        print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
        print("\n------------ photoHandler Debug : message \n")
        print(message)
        print("\n------------ photoHandler Debug : user_data  \n")
        print(user_data)
        print("\n------------ photoHandler Debug : file_id \n")
        print(file_id)
        print("\n------------ photoHandler Debug : naming : name , first , last  \n")
        print(name)
        print(first_name)
        print(last_name)
        print("\n------------ photoHandler Debug : caption \n")
        print(caption)
        print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    # DEBUG ---------------------------------------------------------


        # Photo art input from the bot 
        # send to admin group for moderation 
        # send to the channel if approved 
        
        # Keyboard : the inline keyboard markup that dictates the layout of the buttons.
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "Accept", callback_data=f"accept_art({user_data.id})"),
                InlineKeyboardButton(
                    "Reject", callback_data=f"reject_art({user_data.id})")
            ],
        ])
    # bot sends photo for moderation by admins 
        context.bot.send_photo(
            chat_id=admin_group_id,
            photo=message.photo[0].file_id,
            caption=f"""
    {name}  @{username}

    Description  :
    {caption}
    """,    parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard)
    # Bot echos back to the user for conformaiton of message delivery
    # needs bot to have been in contact with user as the bot cant message new people
        context.bot.send_message(
            chat_id=user_data.id, text="I have sent your art to the admins for moderation , hang tight . ")








def videoHandler(update, context):
    """handle video from the bot : 
    video art input from the bot 
    send to admin group for moderation 
    send to the channel if approved 
    
    """

    
    # Constants 
    # message : the message sent to the bot 
    message = update.effective_message
    # userdata : the user id and stuff from the bot 
    user_data = message.from_user
    # caption : the message caption of the message sent to the bot 
    if message.chat['type'] == 'private':
        print("is a pm ")
        caption = message.caption
        # file id : the unique id of the video sent to the bot 
        file_id = message.video.file_unique_id
        
        first_name = message.chat.first_name

        last_name = message.chat.last_name
        name = ''
        username = message.chat.username
        if first_name:
            name = name + first_name
            if last_name:
                name = name + ' ' + last_name

    # DEBUG ---------------------------------------------------------
        print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
        print("\n------------ videoHandler Debug : message \n")
        print(message)
        print("\n------------ videoHandler Debug : user_data  \n")
        print(user_data)
        print("\n------------ videoHandler Debug : file_id \n")
        print(file_id)
        print("\n------------ videoHandler Debug : naming : name , first , last  \n")
        print(name)
        print(first_name)
        print(last_name)
        print("\n------------ videoHandler Debug : caption \n")
        print(caption)
        print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    # DEBUG ---------------------------------------------------------


        # Photo art input from the bot 
        # send to admin group for moderation 
        # send to the channel if approved 
        
        # Keyboard : the inline keyboard markup that dictates the layout of the buttons.
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "Accept", callback_data=f"accept_art({user_data.id})"),
                InlineKeyboardButton(
                    "Reject", callback_data=f"reject_art({user_data.id})")
            ],
        ])
    # bot sends photo for moderation by admins 
        context.bot.send_video(
            chat_id=admin_group_id,
            video=message.video.file_id,
            caption=f"""
    {name}  @{username}

    Description  :
    {caption}
    """,    parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard)
    # Bot echos back to the user for conformaiton of message delivery
    # needs bot to have been in contact with user as the bot cant message new people
        context.bot.send_message(
            chat_id=user_data.id, text="I have sent your art to the admins for moderation , hang tight . ")











# Accept handler 
def accept_button(update, context):
    """handles the art accept button 
    """
# Constants 
    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    caption = message.caption
    query = update.callback_query
    print("\n----------- accept_button Debug : message  \n")
    print(message)
    print("\n----------- accept_button Debug : data  \n")
    print(data)
    if data['message']['photo']:
        print ('accepting a photo file ')
        file_id = data['message']['photo'].file_id
    if data['message']['video']:
        print ('accepting a video file ')
        file_id = data['message']['video'].file_id
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
    
# DEBUG ---------------------------------------------------------
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    # original_author_id = re.match("[0123456789]", original_author.group())

    print("\n----------- accept_button Debug : user_data \n")
    print(user_data)
    print("\n----------- accept_button Debug : Admin status \n")
    if user_data.id in admins_id_list:
        print("✔️  Is Admin")
    else:
        print("⚠️  Is NOT Admin.")
    print("\n----------- accept_button Debug : file_id  \n")
    print(file_id)
    print("\n----------- accept_button Debug : caption \n")
    print(caption)
    print("\n----------- accept_button Debug : original_author \n")
    print(original_author)
    print("\n----------- accept_button Debug : original_author_id \n")
    print(original_author_id)
    
    print(int(original_author_id_int))
    # print(type(original_author.group()))
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
# DEBUG ---------------------------------------------------------

    if user_data.id in admins_id_list:
        print("All Good , This User is An Admin, Executing Command.")
        context.bot.send_message(chat_id=orig_author_id,
                                 text="Congrats your art has been accepted and posted to the EMVC channel")
        # deletes the message i guess ? on the admin group 
        context.bot.delete_message(
            chat_id=admin_group_id, message_id=message.message_id)
        # sends the photo/video to the channel 
        
        if data['message']['photo']:
            print ('sending a photo file ')
            context.bot.send_photo(chat_id=art_channel_id, photo=file_id, caption=f"""
{caption}
""")
        if data['message']['video']:
            print ('sending a video file ')
            context.bot.send_video(chat_id=art_channel_id, video=file_id, caption=f"""
{caption}
""")

    else:
        print("Non-Admin User trying to accept art , Ignoring .")

# Reject handler
def reject_button(update, context):
    """handles the art reject button 
    """
# Constants 
    message = update.effective_message
    data = update.callback_query
    user_data = data.from_user
    query = update.callback_query
    if data['message']['photo']:
        print ('accepting a photo file ')
        file_id = data['message']['photo'].file_id
    if data['message']['video']:
        print ('accepting a video file ')
        file_id = data['message']['video'].file_id
    original_author = re.match(r"reject_art\((.+?)\)", query.data)
    original_author_str = original_author.group()
    original_author_id = re.findall(r"\d", original_author_str)
    original_author_id_int = ""
    for x in original_author_id:
        original_author_id_int = original_author_id_int + x
    orig_author_id = int(original_author_id_int)
# DEBUG ---------------------------------------------------------
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    print("\n----------- reject_art message  ----------\n")
    print(message)
    print("\n----------- reject_art user_data ---------\n")
    print(user_data)
    print("\n----------- reject_art file_id  ----------\n")
    print(file_id)
    print("\n---------------------------------------------\n")
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
# DEBUG ---------------------------------------------------------
    if user_data.id in admins_id_list:
        print("All Good , This User is An Admin, Executing Command.")
        # echos back to the original user that their art has been rejected 
        context.bot.send_message(
            chat_id=orig_author_id, text="Sorry your art has been rejected, possible reasons can be breaking the rules, check @EMVC_Rules")
        # deletes the message in the admin group 
        context.bot.delete_message(
            chat_id=admin_group_id, message_id=message.message_id)
    else:
        print("Non-Admin User trying to reject art , Ignoring .")


# ----------------------------------------------------------------
# Dispatchers and Handlers go here
ACCEPT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    accept_button, pattern=r"accept_art")
REJECT_CALLBACK_QUERY_HANDLER = CallbackQueryHandler(
    reject_button, pattern=r"reject_art")

dp = updater.dispatcher  # Declaring the dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.photo, photoHandler))
dp.add_handler(MessageHandler(Filters.video, videoHandler))
dp.add_handler(ACCEPT_CALLBACK_QUERY_HANDLER)
dp.add_handler(REJECT_CALLBACK_QUERY_HANDLER)

# ----------------------------------------------------------------
# Webhook stuff
# ⚠ DO NOT TOUCH !
# unless you know what you doing
updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://emvc-bot.herokuapp.com/" + TOKEN)
updater.idle()
