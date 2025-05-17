# accounts/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase



class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@exampe.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_uesr = User.objects.create_superuser(
            username = "testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )
        
        self.assertEqual(admin_uesr.username, "testsuperuser")
        self.assertEqual(admin_uesr.email, "testsuperuser@example.com")
        self.assertTrue(admin_uesr.is_active)
        self.assertTrue(admin_uesr.is_staff)
        self.assertTrue(admin_uesr.is_superuser)
        