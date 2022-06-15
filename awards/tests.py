from django.test import TestCase
from .models import Profile, Project, Ratings
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='dev-git', password='Serial2!')
        self.user.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
    def test_save_user(self):
        self.user.save()
    def test_delete_user(self):
        self.user.delete()
