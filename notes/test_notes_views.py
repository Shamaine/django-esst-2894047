import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client):
    user= User.objects.create_user('Kim','kim@test.com','password')
    client.login(username= user.username, password = 'password')
