import telebot
import os
import random
bot = telebot.TeleBot('8586339682:AAGr8SLSyjOi8NrwVqcogvCdfWQvQwJfNXo')
@bot.message_handler(commands=['mem'])
def send_mem(messeng:True):
    randomlist = os.listdir('images')
    randommage = random.choice(randomlist)
    with open( f'images/{randommage}' , 'rb') as f:
        bot.send_photo(messeng.chat.id, f)
bot.polling()
@bot.message_handler(commands=['pet'])
def send_mem(messeng:True):
    randomlist = os.listdir('ani')
    randommage = random.choice(randomlist)
    with open( f'ani/{randommage}' , 'rb') as f:
        bot.send_photo(messeng.chat.id, f)
bot.polling()