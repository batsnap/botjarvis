# -*- coding: utf-8 -*-

import telebot
import allinfo
import lessons
bot = telebot.TeleBot('947165009:AAH2VH_oMqlIyibz03CeBxzbodVEiMhVbBY')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Weather', 'понедельник', 'вторник','среда','четверг','пятница','суббота')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start. Это бот батыра курбанова. Он показывает погоду и расписание лекций.', reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if  message.text.lower() == 'понедельник':
        k=lessons.Monday()
        bot.send_message(message.chat.id,text=k)
    elif message.text.lower() == 'weather':
        bot.send_message(message.chat.id,text=allinfo.pogoda())
    elif message.text.lower() == 'вторник':
        bot.send_message(message.chat.id,lessons.Tuesday())
    elif message.text.lower() == 'среда':
        bot.send_message(message.chat.id,lessons.Wendsday())
    elif message.text.lower() == 'четверг':
        bot.send_message(message.chat.id,lessons.Tursday())
    elif message.text.lower() == 'пятница':
        bot.send_message(message.chat.id,lessons.Friday())
    elif message.text.lower() == 'суббота':
        bot.send_message(message.chat.id,lessons.Saturday())
        
bot.polling(none_stop=True)