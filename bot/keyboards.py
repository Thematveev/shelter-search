from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def shelter_options(gm_url, shelter_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Google Maps', url=gm_url),
        InlineKeyboardButton('👍', callback_data=f'like,{shelter_id}'),
        InlineKeyboardButton('👎', callback_data=f'dislike,{shelter_id}'),
    )
    return markup


def chancel_process():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(KeyboardButton("Відмінити"))
    return markup

def add_shelter_process():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(KeyboardButton("Відмінити"), KeyboardButton("Відправити геопозицію", request_location=True))
    return markup


def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('Знайти сховище', request_location=True),
        KeyboardButton('Додати сховище')
    )
    return markup