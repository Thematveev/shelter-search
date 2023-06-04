from . import bot
from telebot.types import Message
# from kml_reader import load_shelters
from geopy.distance import geodesic
from .keyboards import shelter_options
import math
from database import Shelter

# shelters = load_shelters()

@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(
        message.chat.id,
        "Привіт. Я бот який допоможе знайти найближче укриття. Для початку пошуку скинь мені точку на карті"
    )


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
        bot.send_message(
            message.chat.id,
            f"{shelter.street}\nДистанція: {shelter.dist} метрів",
            reply_markup=shelter_options(f"http://maps.google.com/maps?q={shelter.lat},{shelter.lon} ")
        )

    


    

