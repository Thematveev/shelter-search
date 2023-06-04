from peewee import Model, FloatField, CharField, AutoField
from . import db


class Shelter(Model):
    id = AutoField()
    city = CharField()
    street = CharField()
    lat = FloatField()
    lon = FloatField()

    class Meta:
        database = db
        db_table = "shelters"


Shelter.create_table()