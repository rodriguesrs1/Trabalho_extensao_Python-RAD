from peewee import Model, CharField, DateField
from database.database import db


class Cliente(Model):
    Nome = CharField()
    email = CharField()
    data_registro = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.