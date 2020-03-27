import telebot

from django.core.management.base import BaseCommand
from django.conf import settings

from .notification import *
from .datadase import *

bot = telebot.TeleBot(token=settings.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text=MESSAGE_START, parse_mode='HTML')


@bot.message_handler(commands=['panel'])
def admin_panel(message):
    bot.send_message(chat_id=message.chat.id, text=ADMIN_MESSAGE, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def search_group(message):
    try:
        if find_group(message.text.lower()) == message.text.lower():
            bot.send_message(chat_id=message.chat.id, text=CHOICE_MASSAGE, parse_mode='HTML',
                             reply_markup=button(message.text))
    except:
        bot.send_message(chat_id=message.chat.id, text=ERROR_MASSAGE, parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.send_message(chat_id=call.message.chat.id, text='\n'.join(get_schedule(call.data)), parse_mode='HTML')


class Commands(BaseCommand):
    help = 'Телеграм-бот'

    bot.polling(none_stop=True)
