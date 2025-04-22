from imports import *

bot = telebot.TeleBot(cloud_bot_api)

@bot.message_handler(commands=['start'])
def send_buttons(message):
    markup = telebot.types.InlineKeyboardMarkup()
    
    button1 = telebot.types.InlineKeyboardButton("Button 1", callback_data='button1')
    button2 = telebot.types.InlineKeyboardButton("Button 2", callback_data='button2')
    
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        execute_function1(call)
    elif call.data == 'button2':
        execute_function2(call)

def execute_function1(call):
    bot.answer_callback_query(call.id, "Function 1 executed!")
    bot.send_message(call.message.chat.id, "call 1")

def execute_function2(call):
    bot.answer_callback_query(call.id, "Function 2 executed!")

bot.polling()
