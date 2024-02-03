import telebot
from random import randint, choice
bot = telebot.TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")

games_key = ['камень','ножницы','бумага']
bot_points = 0
user_points = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   bot.reply_to(message, "Howdy, how are you doing?")
   bot.send_message(message.chat.id, "hii")

@bot.message_handler(commands=['random'])
def random(message):
   m = message.text.split()
   n = randint(int(m[1]), int(m[2]))
   bot.send_message(message.chat.id, f'Random number - {n}')

@bot.message_handler(func=lambda message: message.text in games_key)
def game(message):
    global user_points, bot_points
    user_step = message.text.lower()
    bot_step = choice(games_key)
    bot.reply_to(message, bot_step)
    if (user_step == 'камень' and bot_step == 'ножницы') or \
            (user_step == 'ножницы' and bot_step == 'бумага') or \
            (user_step == 'бумага' and bot_step == 'камень'):
        user_points += 1
        answer = 'ты выйграл, игрок:', user_points, 'бот:', bot_points
    elif user_step == bot_step:
        answer = 'ничья, игрок:', user_points, 'бот:', bot_points
    else:
        bot_points += 1
        answer = 'ты проиграл, игрок:', user_points, 'бот:', bot_points
    bot.send_message(message.chat.id, print(answer))
    



@bot.message_handler(content_types=['text'])
def echo_all(message):
   #bot.reply_to(message, message.text[::-1])
   m = message.text.lower()
   if m == 'clown':
      bot.send_message(message.chat_id, 'BRUH, its for ME?')

bot.infinity_polling()