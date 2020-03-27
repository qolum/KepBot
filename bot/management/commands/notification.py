from telebot import types

# -------------------------------------------------------------------------------#
MESSAGE_START = "<b>Бот-помічник для зручного перегляду розкладу,\n" \
                "введи назву групи щоб побачити магію)Наприклад ak-16-01</b>"
# -------------------------------------------------------------------------------#
ADMIN_MESSAGE = "<b>Адмін-панель бота\n\nПривіт." \
                " За допомогою цього посилання <a href='http://qolum.pythonanywhere.com/'> ADMIN </a>" \
                " ти можеш отримати доступ до адміністративної панелі.</b>"
# -------------------------------------------------------------------------------#
ERROR_MASSAGE = "<b>Я тебе не зрозумів, введи  ще раз назву групи</b>"
# -------------------------------------------------------------------------------#
CHOICE_MASSAGE = "<b> А тепер вибери день </b>"
# -------------------------------------------------------------------------------#

def button(group_name):
    days = types.InlineKeyboardMarkup(row_width=5)
    daymon = types.InlineKeyboardButton("Понеділок", callback_data=f"1,{group_name}")
    daytue = types.InlineKeyboardButton("Вівторок", callback_data=f"2,{group_name}")
    daywed = types.InlineKeyboardButton("Середа", callback_data=f"3,{group_name}")
    daythu = types.InlineKeyboardButton("Четверг", callback_data=f"4,{group_name}")
    dayfri = types.InlineKeyboardButton("П'ятниця", callback_data=f"5,{group_name}")
    days.add(daymon, daytue, daywed, daythu, dayfri)
    return days
# -------------------------------------------------------------------------------#
