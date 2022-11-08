import telebot
from telebot import types
import urllib

TOKEN = ""
bot = telebot.TeleBot(TOKEN)
typ = types.InlineKeyboardMarkup





@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на рандомный сайт --", url='http://randompage.ru/generate')
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на абсолютно рандомный сайт)".format(message.from_user), reply_markup=markup)
    



@bot.message_handler(content_types=['text'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    typ = types.InlineKeyboardMarkup
    bot.send_message(chat_id, "Пиши /start :)")


bot.polling(non_stop=True)