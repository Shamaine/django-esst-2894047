import factory
from django.contrib.auth.models import User
from notes.models import Notes
from factory import fuzzy
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username= factory.Sequence(lambda n: f"user_{n:04}") #user_0000
    email=factory.LazyAttribute(lambda user: f"{user.username}@example.com")
    #encrypt the password in the database
    password=factory.LazyAttribute(lambda p: make_password('password'))

class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notes
    title=fuzzy.FuzzyText(length =20)
    text =fuzzy.FuzzyText(length =200)
    #create a brand new user for you id u do not have one while creating the note
    user = factory.SubFactory(UserFactory) 