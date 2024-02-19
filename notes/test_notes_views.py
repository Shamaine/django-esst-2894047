import pytest
from django.contrib.auth.models import User
from notes.models import Notes
from .factories import UserFactory,NoteFactory
#use pytest.fixture to create reusable code
@pytest.fixture
def logged_user(client):
    user= UserFactory()
    client.login(username= user.username, password = 'password')
    return user

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client,logged_user):
 
    note = NoteFactory(user=logged_user)
    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content=str(response.content)
    assert note.title in content
    assert 1 ==content.count('<h3>')

@pytest.mark.django_db
def test_create_endpoint_receives_form_data(client,logged_user):
    form_data = {'title':'An Impressive title', 'text':'A really interesting text'}

    response =client.post(path='/smart/notes/new',data = form_data,follow=True)

    assert 200 == response.status_code

    #check if we receive the final template we expect
    assert 'notes/notes_list.html' in response.template_name
    # to make sure the user has at least 1 note
    assert 1 ==logged_user.notes.count()



