import telebot
import requests
import json

bot = telebot.TeleBot('5742035515:AAEPlSgKWKHm7kDPY9XhV-kJHXihddw-Wgk')

city_name = ''
todo = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'привет этот бот показывает прогноз погоды \n '
                                      f'нажмите на /current чтобы узнать прогноз погоды')


@bot.message_handler(commands=['current'])
def current_weather(message):
    bot.send_message(message.chat.id, f'введите ваш город:')

    @bot.message_handler(content_types=['text'])
    def getWeather(message):
        global city_name
        global todo
        city_name = message.text
        response = requests.get(
            f'http://api.weatherapi.com/v1/current.json?key=7acb4d7a8e08451a95a15435220210&q={city_name}&aqi=no')
        todo = json.loads(response.text)
        bot.send_message(message.chat.id, f'в городе {city_name} температура: {todo["current"]["temp_c"]}')
        # print(f'в городе {city_name} температура: {todo["current"]["temp_c"]}')


# name = ''
# age = 0
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == "/reg":
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, "Напиши /reg")
#
#
# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)
#
#
# def get_age(message):
#     global age
#     try:
#         age = int(message.text)
#     except Exception:
#         bot.send_message(message.from_user.id, 'Введите цифрами:')
#     keyboard = types.InlineKeyboardMarkup()
#     key_yes = types.InlineKeyboardButton(text="да", callback_data='yes')
#     key_no = types.InlineKeyboardButton(text='нет', callback_data='no')
#     keyboard.add(key_yes, key_no)
#     question = 'тебя зовут' + name + ' и тебе' + str(age) + 'лет? '
#
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == 'yes':
#         bot.send_message(call.message.chat.id, 'запомню=)')
#     elif call.data == 'no':
#         bot.send_message(call.message.chat.id, "Как тебя зовут?")
#         bot.register_next_step_handler(call.message, get_name)


bot.polling(none_stop=True, interval=0)
