from unittest.mock import patch
from test_plus import TestCase

from accounts.models import User


class AuthenticateTest(TestCase):
    base_url = '/accounts/auth/'

    @patch('accounts.models.User.find_by_credentials')
    def test_auth_success(self, mock):
        mock.return_value = User()

        payload = {
            'username': 'hello',
            'password': 'hello',
        }
        res = self.post(self.base_url, data=payload)
        self.assertEqual(res.status_code, 200)

    @patch('accounts.models.User.find_by_credentials')
    def test_auth_failure(self, mock):
        mock.return_value = None

        res = self.get(self.base_url)
        self.assertEqual(405, res.status_code)

        res = self.post(self.base_url)
        self.assertEqual(400, res.status_code)

        payload = {
            'username': 'hello',
            'password': 'hello',
        }
        res = self.post(self.base_url, data=payload)
        self.assertEqual(401, res.status_code)
