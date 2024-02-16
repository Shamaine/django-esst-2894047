import pytest
from django.contrib.auth.models import User
from notes.models import Notes
from .factories import UserFactory
#use pytest.fixture to create reusable code
@pytest.fixture
def logged_user(client):
    user= UserFactory()
    client.login(username= user.username, password = 'password')
    return user

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client,logged_user):
 
    note = Notes.objects.create(title='An interesting title', text='',user=logged_user)
    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content=str(response.content)
    assert "An interesting title" in content
    assert 1 ==content.count('<h3>')
