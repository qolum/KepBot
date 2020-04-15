from telebot import types

from .src import *


def start_button():
    button = types.InlineKeyboardMarkup()
    teachers = types.InlineKeyboardButton("Вчитель", callback_data='teacher')
    student = types.InlineKeyboardButton("Студент", callback_data='student')
    button.add(student, teachers)
    return button


def back_button(name):
    button = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("Назад", callback_data=name)
    button.add(back)
    return button


def main_button(name):
    button = types.InlineKeyboardMarkup(row_width=5)
    daymon = types.InlineKeyboardButton("Пн", callback_data=f"['schedule', 1, '{name}']")
    daytue = types.InlineKeyboardButton("Вт", callback_data=f"['schedule', 2, '{name}']")
    daywed = types.InlineKeyboardButton("Ср", callback_data=f"['schedule', 3, '{name}']")
    daythu = types.InlineKeyboardButton("Чт", callback_data=f"['schedule', 4, '{name}']")
    dayfri = types.InlineKeyboardButton("Пт", callback_data=f"['schedule', 5, '{name}']")
    find_lect = types.InlineKeyboardButton("Де в мене пара", callback_data=f"['find', '{name}']")
    back = types.InlineKeyboardButton("Назад", callback_data='back')
    button.add(daymon, daytue, daywed, daythu, dayfri)
    button.add(find_lect, back)
    return button


def search_result_button(name):
    button = types.InlineKeyboardMarkup()
    if get_teachers(name) != 'Empty':
        for item in range(len(get_teachers(name))):
            b = types.InlineKeyboardButton(get_teachers(name)[item], callback_data=get_teachers(name)[item])
            button.add(b)
    elif get_groups(name) != 'Empty':
        for item in range(len(get_groups(name))):
            b = types.InlineKeyboardButton(get_groups(name)[item], callback_data=get_groups(name)[item])
            button.add(b)
    else:
        button = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        back = types.KeyboardButton("Ти не ввів правильно данні попробуй ще раз")
        button.add(back)
    return button
