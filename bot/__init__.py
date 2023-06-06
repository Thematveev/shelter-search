from telebot import TeleBot
import config

bot = TeleBot(config.TOKEN)

from . import handlers
from . import callback_handlers
from . import add_shelter_handlers