import pytest
from django.contrib.auth.models import User

def test_home_view(client):
    response = client.get(path='/')
    assert response.status_code==200
    assert 'Welcome to SmartNotes!' in str(response.content)
 
def test_signup(client):
    response = client.get(path='/signup')
    assert response.status_code==200
    assert 'home/register.html' in response.template_name 


#create temporary test database
@pytest.mark.django_db
def test_signup_authenticated(client):
    user= User.objects.create_user('Kim','kim@test.com','password')
    client.login(username= user.username, password = 'password')
    #follow= true means follow the url status code in this example a url is redirected will return code 302
    response = client.get(path='/signup',follow=True)
    assert 200 == response.status_code
    assert 'notes/notes_list.html' in response.template_name 