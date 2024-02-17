import json
from telebot import TeleBot, types
from random import choice




bot = TeleBot("6974950222:AAFzS-4hp_6NM6unzhdnB9kRnGZC6GAgk_I")
game = False
game_city = False
used_cities = []
letter = ''
leaderboard = {}

indx = 0
points = 0





with open('victorina.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = []
    for line in f.readlines():
        cities.append(line.strip().lower())


        

def get_next_question(data, indx):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(4):
        btn = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(btn)
    markup.add(types.KeyboardButton("Выход"))
    return markup

def select_letter(text):
    i = 1
    while text[-1*i] in ('ь', 'ы', 'й'):
        i += 1
    return text[-1*i]


@bot.message_handler(commands=['города'])
def start_game(message):
    global game
    global letter
    game_city = True
    city = choice(cities)
    letter = select_letter(city)
    bot.send_message(message.chat.id, text=city)



@bot.message_handler(commands=['points'])
def get_points(message):
    bot.send_message(message.chat.id, text=f'Набрано очков: {points}')
 
@bot.message_handler(commands=['сохранить'])
def save(message):
    with open('scores.json', 'w', encoding='utf-8') as first_name:
        json.dump(leaderboard, f)
    bot.send_message(message.chat.id, 'прогресс сохранен')



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

    if game_city:
        if message.text.lower() in used_cities:
            print(letter)
            bot.send_message(message.chat.id, 'Город назывался!')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'Не та буква!')
            return
        if message.text.lower() in data:
            if message.from_user.first_name in leaderboard:
                leaderboard[message.from_user.first_name] += 1
            else:
                leaderboard[message.from_user.first_name] = 1


bot.infinity_polling()
