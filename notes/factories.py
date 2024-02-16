import factory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username= factory.Sequence(lambda n: f"user_{n:04}") #user_0000
    email=factory.LazyAttribute(lambda user: f"{user.username}@example.com")
    #encrypt the password in the database
    password=factory.LazyAttribute(lambda p: make_password('password'))