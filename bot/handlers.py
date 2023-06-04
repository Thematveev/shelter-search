from . import bot
from telebot.types import Message
# from kml_reader import load_shelters
from geopy.distance import geodesic
from .keyboards import shelter_options
import math
from database import Shelter, User, Votes
import peewee

# shelters = load_shelters()

@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(
        message.chat.id,
        "Привіт. Я бот який допоможе знайти найближче укриття. Для початку пошуку скинь мені точку на карті"
    )
    try:
        User.create(
            uid=message.from_user.id,
            username=message.from_user.username,
            firstname=message.from_user.first_name,
            lastname=message.from_user.last_name
        )
    except peewee.IntegrityError:
        pass


@bot.message_handler(content_types=['location'])
def location_handler(message: Message):
    # bot.send_message(
    #     message.chat.id,
    #     f"Ваші координати такі:\nLatitude: {message.location.latitude}\nLongitude: {message.location.longitude}\nПочинаю пошук..."
    # )
    
    shelter_list = list(Shelter.select())
    user_cordinates = [message.location.longitude, message.location.latitude]

    for shelter in shelter_list:
        shelter.dist = math.floor(geodesic(user_cordinates, [shelter.lon, shelter.lat]).meters)
        # print(i.dist, type(i.dist))

    shelter_list.sort(key=lambda x: x.dist)

    # print(shelters[:5])

    bot.send_message(
            message.chat.id,
            f"Ось 5 найближчих сховищ"
        )
    # print(shelters)
    for shelter in shelter_list[:5]:
        positive_votes = Votes.select().where(Votes.is_positive == True).where(Votes.shelter == shelter).count()
        negative_votes = Votes.select().where(Votes.is_positive == False).where(Votes.shelter == shelter).count()

        bot.send_message(
            message.chat.id,
            f"[{shelter.type}]\n{shelter.street}\nОпис та орієнтир:\n{shelter.description if shelter.description else 'Нема даних'}\nДистанція: {shelter.dist} метрів\nРейтинг:\n👍: {positive_votes}\n👎: {negative_votes}",
            reply_markup=shelter_options(
            f"http://maps.google.com/maps?q={shelter.lat},{shelter.lon} ",
            shelter_id=shelter.id
            )
        )

    


    

