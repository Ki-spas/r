import telebot
#from bot_logic import gen_pass 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

    
bot = telebot.TeleBot("8586339682:AAGr8SLSyjOi8NrwVqcogvCdfWQvQwJfNXo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, " ПОПАЛСЯ КАШАТНИК!34561")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "ПОПАЛСЯ СОБАЧНИК!!!!!!1")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "КОТЫ ЛУЧШЕ СОБАК?!!!!!!", reply_markup=gen_markup())

bot.infinity_polling()
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "в этом боте несколько команд:start , hello , bue , и опрос,который появляется при любом сообщение , также команда help !")