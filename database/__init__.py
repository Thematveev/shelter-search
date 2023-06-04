from peewee import SqliteDatabase

db = SqliteDatabase('./data.db')

from .models import *