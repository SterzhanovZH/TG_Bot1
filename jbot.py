import requests
import telebot


bot = telebot.TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")


def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.message_handler(commands=['duck'])
def duck(message):
   url = random_duck()
   bot.send_message(message.chat.id, url)


bot.infinity_polling()