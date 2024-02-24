import telebot
from telebot import types
from random import randint



bot = telebot.TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")


sum_check = 0

with open('bad_words.txt', "r", encoding='utf-8') as f:
    data = [word.strip().lower() for word in f.readlines()] 


def is_group(message):
    return message.chat.type in ('group', 'supergroup')

def has_bad_words(text):
    message_words = text.split(' ')
    for word in message_words:
        if word in data:
            return True
    return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='start')


'''@bot.message_handler(func=lambda message: has_bad_words(message.text.lower()) and is_group(message))
def start(message):'''


'''@bot.message_handler(func=lambda message: message.text.lower() in data and is_group(message))
def start(message):'''

@bot.message_handler(commands=["check"])
def default_test(message):
    global sum_check
    keyboard = types. InlineKeyboardMarkup()
    numbers = ["один", "два", "три", "четыре", "пять"
    "шесть", "семь", "Восемь", "девять", "десять"]
    keys = []
    for indx, number in enumerate(numbers):
        keys.append(types. InlineKeyboardButton(text=number, callback_data=indx+1))
    keyboard.row(*keys)

    n1 = randint(1, 5)
    n2 = randint(1, 5)
    sum_check = n1 + n2
    bot.send_message(message.chat.id, f"Pешитe пример: {1} + {n2} = ?", reply_markup=keyboard)
    

@bot.callback_query_handler (func=lambda call: call.data)
def callback_inline(call):
    global sum_check
    if int(call.data) == sum_check:
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Проверка пройдена")
    if int(call.data) != sum_check:
        bot.ban_chat_member(call.message.chat.id, call.from_user.id)

bot.infinity_polling()