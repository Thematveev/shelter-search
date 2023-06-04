from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def shelter_options(gm_url, shelter_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('Google Maps', url=gm_url),
        InlineKeyboardButton('👍', callback_data=f'like,{shelter_id}'),
        InlineKeyboardButton('👎', callback_data=f'dislike,{shelter_id}'),
    )
    return markup