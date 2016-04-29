# -*- coding: utf-8 -*-
import config
from config import *
import telebot
import time
bot = telebot.TeleBot(config.token)


# def listener(messages):
#    for m in messages:
#        if m.content_type == 'text':
#            bot.send_message(m.chat.id, m.text)


@bot.message_handler(commands=['week'])
def handle_message(message):
    bot.send_message(message.chat.id, give_syllabus_full_week())


@bot.message_handler(commands=['num_week'])
def handle_message(message):
    bot.send_message(message.chat.id, check_num_week())


@bot.message_handler(commands=['type_week'])
def handle_message(message):
    bot.send_message(message.chat.id, check_type_week())


@bot.message_handler(regexp='today')
def handle_message(message):
    bot.send_message(message.chat.id, give_syllabus())


@bot.message_handler(commands=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])
def handle_message(message):
    bot.send_message(message.chat.id, give_syllabus(text=den[message.text]))


@bot.message_handler(regexp='data')
def handle_message(message):
    bot.send_message(message.chat.id, check_day())


@bot.message_handler(regexp='tomorrow')
def handle_message(message):
    bot.send_message(message.chat.id, give_syllabus(n=1))


@bot.message_handler(commands=['real_week'])
def handle_message(message):
    bot.send_message(message.chat.id, check_num_week(1))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, info)
#   bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Всё хорошо, живу')
    elif message.text == 'Привет' or message.text == 'Hello':  #or message.text == 'Прив' or message.text == 'Hi' or message.text == 'Здравствуй':
        bot.send_message(message.chat.id, '110100001001111111010001100000001101000010111000110100'
                                          '001011001011010000101101011101000110000010, то есть - привет')
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    # bot.set_update_listener(listener)
    bot.polling(none_stop=True)
#    while True:
#       time.sleep(200)
