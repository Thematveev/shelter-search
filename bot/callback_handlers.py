from . import bot
from database.models import Votes, User, Shelter

@bot.callback_query_handler(lambda cbl: True)
def rating_handler(cbl):
    type, shelter_id = cbl.data.split(',')
    shelter_id = int(shelter_id)
    user = User.get(uid=cbl.from_user.id)
    shelter = Shelter.get(Shelter.id == shelter_id)
    vote = Votes.select().where(Votes.user == user).where(Votes.shelter == shelter)
    if len(list(vote)) == 0:
        Votes.create(
            user=user,
            shelter=shelter,
            is_positive= True if type == 'like' else False
        )
        bot.answer_callback_query(cbl.id, "Ваш голос враховано")
    else:
        bot.answer_callback_query(cbl.id, "Нажаль ви вже голосували за це сховище")