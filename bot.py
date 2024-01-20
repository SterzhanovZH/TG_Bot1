import telebot
from random import randint
bot = telebot.TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.reply_to(message, "Howdy, how are you doing?")
   bot.send_message(message.chat.chat_id, "hii")

@bot.message_handler(commands=['random'])
def random(message):
   m = message.text.split()
   n = randint(int(m[1]), int(m[2]))
   bot.send_message(message.chat.id, f'Random number - {n}')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
   #bot.reply_to(message, message.text[::-1])
   m = message.text.lower()
   if m == 'clown':
      bot.send_message(message.chat_id, 'BRUH, its for ME?')

bot.infinity_polling()