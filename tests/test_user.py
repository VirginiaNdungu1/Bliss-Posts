import unittest
from app.models import User


class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='guava')

    def test_pwd_write_denied(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_set_password(self):
        self.assertTrue(self.new_user.user_pwd is not None)

    def test_check_password(self):
        self.assertTrue(self.new_user.verify_password('guava'))
