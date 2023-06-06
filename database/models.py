from peewee import Model, FloatField, CharField, BooleanField, ForeignKeyField
from . import db


class Shelter(Model):
    city = CharField(null=True)
    street = CharField(null=True)
    lat = FloatField()
    lon = FloatField()
    type = CharField(default='official')
    description = CharField(null=True)

    class Meta:
        database = db
        db_table = "shelters"

class User(Model):
    uid = CharField(unique=True)
    username = CharField(null=True)
    firstname = CharField(null=True)
    lastname = CharField(null=True)


    class Meta:
        database = db
        db_table = "users"


class Votes(Model):
    is_positive = BooleanField()
    user = ForeignKeyField(User)
    shelter = ForeignKeyField(Shelter)


    class Meta:
        database = db
        db_table = "votes"


Shelter.create_table()
User.create_table()
Votes.create_table()
