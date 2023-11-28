from django.test import LiveServerTestCase, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from rewear_app.forms import PostForm
from rewear_app.models import *
import time


# manage.py test rewear_app.tests.PostModelTest

class Hosttest(LiveServerTestCase):

    def testhomepage(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        time.sleep(1)
        assert "Rewear App" in driver.title

class LoginFormTest(LiveServerTestCase):
    def testfrom(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/accounts/login/')
        time.sleep(1)
        #22 mins in
        user_name = driver.find_element(By.ID, 'id_username')
        user_password = driver.find_element(By.ID, 'id_password')
        submit = driver.find_element(By.ID, 'submit')
        time.sleep(1)
        user_name.send_keys('USER1')
        user_password.send_keys('qwertyui12345678')
        submit.send_keys(Keys.RETURN)

        assert 'Logout USER1' in driver.page_source


class MyViewTestCase(TestCase):  
    def test_my_view(self):  
        response = self.client.get(reverse('index'))  
        self.assertEqual(response.status_code, 200)


class MyFormTestCase(TestCase):  
    def test_valid_form(self):  
        form_data = {
            'image': '~/Users/Jstar/Downloads/IMG_9451.jpg',
            'title': 'Test Title',
            'type': 'Tops',
            'brand': 'Test Brand',
            'size': 'M',
            'more_sizing': False,
            'about': 'This is a test about section.',
            'contact_info': 'test@example.com',
        }

        form = PostForm(data=form_data)  
        self.assertTrue(form.is_valid()) 

class MyModelTestCase(TestCase):
    def setUp(self):
        # Create a user instance
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Use the user instance when creating the Post object
        self.model = Post.objects.create(title='Test Title', user=user)

    def test_model_title(self):
        self.assertEqual(self.model.title, 'Test Title')
