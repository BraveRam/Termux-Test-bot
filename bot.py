import telebot
from telebot.types import *

bot = telebot.TeleBot("6064149182:AAH_dlb92sIL--cHGnzuDI7ENEDzFFC-Ut8")

key = ReplyKeyboardMarkup()
k1 = KeyboardButton(text="Phone", request_location = True)
k2 = KeyboardButton(text="Location", request_location = True)
key.add(k1)
key.add(k2)

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, "Heya fron Python", reply_markup = key)

print("Success")
bot.infinity_polling()
