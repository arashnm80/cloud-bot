from imports import *
from json_functions import *
from functions import *

bot = telebot.TeleBot(cloud_bot_api, parse_mode="html")
logger = telebot.logger

# add message to active folder
@bot.message_handler(commands=['add_m'])
def add_message(message):
    # check if message is reply to sth
    replied_msg = message.reply_to_message
    if replied_msg is None:
        bot.send_message(message.chat.id, "your /add_m should be reply to a message")
        return
    # check if active folder exists
    json_data = read_user_json(message.chat.id)
    active_f = json_data["settings"]["active_f"]
    if active_f not in json_data["db"]:
        bot.send_message(message.chat.id, f"you should set an active folder for your message.")
        return
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify message name after command")
        return
    message_name = words[1]
    # add message
    json_data["db"][active_f][message_name] = replied_msg.message_id
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, f"message added to folder <b>{active_f}</b>")

# remove message from active folder
@bot.message_handler(commands=['rem_m'])
def rem_message(message):
    # check if active folder exists
    json_data = read_user_json(message.chat.id)
    active_f = json_data["settings"]["active_f"]
    if active_f not in json_data["db"]:
        bot.send_message(message.chat.id, f"you should set an active folder for your message.")
        return
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify message name with a space")
        return
    message_name = words[1]
    # check if message exists
    if message_name not in json_data["db"][active_f]:
        bot.send_message(message.chat.id, f"message doesn't exist in this folder")
        return
    # remove the message
    json_data["db"][active_f].pop(message_name)
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, f"message removed from folder <b>{active_f}</b>")

# see message from active folder
@bot.message_handler(commands=['see_m'])
def see_message(message):
    # check if active folder exists
    json_data = read_user_json(message.chat.id)
    active_f = json_data["settings"]["active_f"]
    if active_f not in json_data["db"]:
        bot.send_message(message.chat.id, f"you should set an active folder for your message.")
        return
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify message name after command")
        return
    message_name = words[1]
    # check if message exists
    if message_name not in json_data["db"][active_f]:
        bot.send_message(message.chat.id, f"message doesn't exist in this folder")
        return
    # get message id from message name
    message_id = json_data["db"][active_f][message_name]
    # return message to user
    bot.send_message(message.chat.id, f"this is message <b>{message_name}</b> from folder <b>{active_f}</b>:")
    bot.copy_message(message.chat.id, message.chat.id, message_id)


# add folder
@bot.message_handler(commands=['add_f'])
def add_folder(message):
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify folder name after command")
        return
    folder_name = words[1]
    json_data = read_user_json(message.chat.id)
    if folder_name not in json_data["db"]:
        json_data["db"][folder_name] = {}
    else:
        bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> already exists")
        return
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> added to folders list")

# remove folder
@bot.message_handler(commands=['rem_f'])
def rem_folder(message):
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify folder name after command")
        return
    folder_name = words[1]
    json_data = read_user_json(message.chat.id)
    if folder_name not in json_data["db"]:
        bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> doesn't exist")    
        return
    json_data["db"].pop(folder_name)
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> removed from folders list")

# set active folder to work with
@bot.message_handler(commands=['set_f'])
def set_folder(message):
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify folder name after command")
        return
    folder_name = words[1]
    json_data = read_user_json(message.chat.id)
    if folder_name not in json_data["db"]:
        bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> doesn't exist")
        return
    json_data["settings"]["active_f"] = folder_name
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> set as active✅")

# see all messages from folder
@bot.message_handler(commands=['see_f'])
def see_folder(message):
    # remove beginning part before space
    words = message.text.split(" ", 1)
    if len(words) == 1:
        bot.send_message(message.chat.id, f"specify folder name after command")
        return
    folder_name = words[1]
    json_data = read_user_json(message.chat.id)
    # check if folder exists
    if folder_name not in json_data["db"]:
        bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> doesn't exist")    
        return
    # check for empty folder
    if not json_data["db"][folder_name]:
        bot.send_message(message.chat.id, f"folder <b>{folder_name}</b> is empty:")
        return
    # all fine
    bot.send_message(message.chat.id, f"these are messages from folder <b>{folder_name}</b>:")
    for message_name, message_id in json_data["db"][folder_name].items():
        bot.copy_message(message.chat.id, message.chat.id, message_id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    if check_user_json_exist(user_id):
        bot.send_message(message.chat.id, "welcome, good to see you again. send /help if you need to see the guide.")
    else:
        create_user_json(user_id)
        bot.send_message(message.chat.id, "welcome, you are a new user. send /help for more information.")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['show'])
def show_everything(message):
    output = ""
    json_data = read_user_json(message.chat.id)
    active_f = json_data["settings"]["active_f"]
    # check for empty db
    if json_data["db"] == {}:
        bot.send_message(message.chat.id, f"There is nothing to show yet.")
        return
    # add folders and messages
    for folder, messages in json_data["db"].items():
        if folder == active_f:
            active_f_sign = "✅"
        else:
            active_f_sign = ""
        output += f"\n<blockquote><b>{folder}</b>{active_f_sign}"
        for message_name, message_id in messages.items():
            output += f"\n• {message_name}"
        output += "</blockquote>"
    bot.send_message(message.chat.id, output)

# erase all messages and folders
@bot.message_handler(commands=['erase'])
def erase_everything(message):
    json_data = read_user_json(message.chat.id)
    json_data["db"] = {}
    write_user_json(message.chat.id, json_data)
    bot.send_message(message.chat.id, "all messages and folders are erased")

#################################################################################

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("Yes", callback_data="yes-add-message-to-db")
    button2 = telebot.types.InlineKeyboardButton("No", callback_data="no-don't-add-message-to-db")
    markup.add(button1, button2)
    bot.reply_to(message, "Do you like to store this messaage?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes-add-message-to-db":
        add_message_to_db(call)
    elif call.data == "no-don't-add-message-to-db":
        pass

    logger.info(call) # to-do : test

# bot.remove_webhook()
bot.infinity_polling()
