import json
from telebot import TeleBot, types




bot = TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")
game = False

indx = 0
points = 0


with open('victorina.json', 'r', encoding='utf-8') as f:
    data = json.load(f)




def get_next_question(data, indx):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(4):
        btn = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(btn)
    markup.add(types.KeyboardButton("Выход"))
    return markup




@bot.message_handler(commands=['points'])
def get_points(message):
    bot.send_message(message.chat.id, text=f'Набрано очков: {points}')




@bot.message_handler(commands=['quizz'])
def quizz(message):
    global game
    global indx
    game = True
    markup = get_next_question(data, indx)
    bot.send_message(
        message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)


@bot.message_handler()
def viktorinas(message):
    global game
    global indx
    global points
    if game:
        if message.text == data[indx]['ответ']:
            bot.send_message(message.chat.id, 'Правильно')
            points += 1
        elif message.text == 'Выход':
            game == False
            bot.send_message(message.chat.id, 'Пока')
            return
        else:

            bot.send_message(message.chat.id, f'Неправильно, правильный ответ - {data[indx]["ответ"]}')
        indx += 1
        markup = get_next_question(data, indx)
        bot.send_message(message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)
