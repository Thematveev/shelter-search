from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def shelter_options(gm_url):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Google Maps', url=gm_url))
    return markup