import telebot

from django.core.management.base import BaseCommand
from django.conf import settings

from .message import *
from .button import *
from .src import *

bot = telebot.TeleBot(token=settings.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text=START_MESSAGE, parse_mode='HTML', reply_markup=start_button())


@bot.message_handler(commands=['admin'])
def admin_panel(message):
    bot.send_message(chat_id=message.chat.id, text=ADMIN_MESSAGE, parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=START_MESSAGE,
                          parse_mode='HTML', reply_markup=start_button())


@bot.callback_query_handler(func=lambda call: call.data == 'teacher' or call.data == 'student')
def main(call):
    if call.data == 'teacher':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=HEllO_TEACHERS_MASSAGE,
                              parse_mode='HTML')
    elif call.data == 'student':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=HEllO_STUDENT_MASSAGE,
                              parse_mode='HTML')


@bot.message_handler(
    func=lambda message: True if (get_teachers(message.text) != [] or get_groups(message.text) != []) else False)
def auto_search(message):
    if get_teachers(message.text):
        bot.send_message(chat_id=message.chat.id,
                         text=CHOICE_NAME_MASSAGE,
                         parse_mode='HTML',
                         reply_markup=search_result_button(message.text))
    elif get_groups(message.text):
        bot.send_message(chat_id=message.chat.id,
                         text=CHOICE_NAME_MASSAGE,
                         parse_mode='HTML',
                         reply_markup=search_result_button(message.text))


@bot.callback_query_handler(
    func=lambda call: True if (call.data in get_teachers(call.data) or call.data in get_groups(call.data)) else False)
def main_view(call):
    if call.data in get_teachers(call.data):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"Добрий день:{call.data}",
                              parse_mode='HTML',
                              reply_markup=main_button(call.data))
    elif call.data in get_groups(call.data):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"Привіт:{call.data}",
                              parse_mode='HTML',
                              reply_markup=main_button(call.data))


@bot.callback_query_handler(func=lambda call: True if (eval(call.data)[0] == 'schedule') else False)
def response_schedule(call):
    if eval(call.data)[2] in get_teachers(eval(call.data)[2]):
        response = get_schedule_for_teacher(call.data)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='\n'.join(response),
                              parse_mode='HTML',
                              reply_markup=back_button(eval(call.data)[2]))

    elif eval(call.data)[2] in get_groups(eval(call.data)[2]):
        response = get_schedule_for_student(call.data)
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='\n'.join(response),
                              parse_mode='HTML',
                              reply_markup=back_button(eval(call.data)[2]))


@bot.callback_query_handler(func=lambda call: True if (eval(call.data)[0] == 'find') else False)
def response_schedule_now(call):
    if eval(call.data)[1] in get_teachers(eval(call.data)[1]):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=get_lecture_for_teacher(eval(call.data)),
                              parse_mode='HTML',
                              reply_markup=back_button(eval(call.data)[1]))
    elif eval(call.data)[1] in get_groups(eval(call.data)[1]):
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='\n'.join(get_lecture_for_student(eval(call.data))),
                              parse_mode='HTML',
                              reply_markup=back_button(eval(call.data)[1]))


@bot.message_handler(content_types=['text'])
def error(message):
    bot.send_message(chat_id=message.chat.id, text=ERROR_MASSAGE, parse_mode='HTML')


class Commands(BaseCommand):
    help = 'Телеграм-бот'

    bot.polling(none_stop=True)
