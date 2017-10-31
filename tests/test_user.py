import unittest
from app.models import User


class userModelTest(unittest.TestCase):

    def setUp(self):
        '''
        function that creates instance of User class
        '''
        self.new_user = User(password='guava')

    def test_set_password(self):
        '''
        test case that ascertains that when a password
        is hashed, the user_pwd contains value
        '''
        self.assertTrue(self.new_user.user_pwd is not None)

    def test_no_access_pwd(self):
        '''
        test case to cofirm that our appliation raises an AttributeError
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_check_password(self):
        '''
        test case confirms that the password_hash can be verified
        when we pass in the correct password
        '''
        self.assertTrue(self.new_user.verify_password('guava'))
