import telebot
import webbrowser
from telebot import types

BOT = telebot.TeleBot('6053672183:AAHsWiGgslTfeR5dgRjcSeliufE_a6Lt5JM')

@BOT.message_handler(commands=['start'])
def start(command):
    BOT.send_message(command.chat.id , '1234')

@BOT.message_handler(commands=['site'])
def site(command):
    webbrowser.open('https://izi.ua/')


BOT.infinity_polling()