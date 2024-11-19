from django.db.models import CharField, Model
from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)


# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING, default=None)
    rating = IntegerField(default=None)
    released = DateField(default=None)
    description = TextField(default=None)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Actor(Model):
    firstname = CharField(max_length=128)
    lastname = CharField(max_length=128)
    birth_date = DateField(default=None)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
