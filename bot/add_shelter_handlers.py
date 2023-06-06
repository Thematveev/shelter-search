from . import bot
from .keyboards import chancel_process, add_shelter_process, main_keyboard
from database.models import Shelter

sessions = dict()

@bot.message_handler(regexp=r'Додати сховище')
def add_shelter_handler(message):
    bot.send_message(message.chat.id, "Зараз ви можете додати сховище. Відправте геолокацію де воно розташоване", reply_markup=add_shelter_process())
    sessions[message.chat.id] = Shelter()
    bot.register_next_step_handler(message, handler_geo)


def handler_geo(msg):
    if msg.content_type == 'location':
        model = sessions.get(msg.chat.id)
        model.lat = msg.location.latitude
        model.lon = msg.location.longitude
        model.type = "user"

        bot.send_message(
            msg.chat.id,
            "Добре, тепер очікую повідомлення з мінмальним описом та орієнтирами",
            reply_markup=chancel_process()
        )
        bot.register_next_step_handler(msg, description_handler)

    elif msg.content_type == 'text' and msg.text == "Відмінити":
        bot.send_message(
            msg.chat.id,
            "Ви відмінили додавання",
            reply_markup=main_keyboard()
        )

def description_handler(msg):
    if msg.content_type == 'text' and msg.text == "Відмінити":
        bot.send_message(
            msg.chat.id,
            "Ви відмінили додавання",
            reply_markup=main_keyboard()
        )
    else:
        descr = msg.text
        model = sessions.get(msg.chat.id)
        model.description = descr
        model.save()
        bot.send_message(
            msg.chat.id,
            "Ви успішно додали сховище!",
            reply_markup=main_keyboard()
        )


