from needed_modules import *

from json_functions import *

bot = telebot.TeleBot(cloud_bot_api)

@bot.message_handler(commands=['add'])
def add_message(message):
    replied_msg = message.reply_to_message
    if replied_msg is None:
        bot.send_message(message.chat.id, "your /add should be reply to a message")
    else:
        bot.send_message(message.chat.id, replied_msg.text)
    # bot.reply_to(message, bot_introduction_msg)
    echo_all(message)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.chat.id
    if check_user_json_exist(user_id):
        json_data = read_user_json(user_id)
        print(json_data)
    else:
        init_user_json(user_id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    pass
    

bot.infinity_polling()
