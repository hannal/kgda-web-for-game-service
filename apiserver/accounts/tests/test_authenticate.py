from unittest.mock import patch
from test_plus import TestCase

from accounts.models import User, AccessToken


class AuthenticateTest(TestCase):
    base_url = '/accounts/auth/'

    def create_patch(self, name):
        patcher = patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    @patch('accounts.models.AccessToken.create')
    @patch('accounts.models.User.find_by_credentials')
    def test_auth_success(self, mock_user, mock_token):
        user = User()
        token = AccessToken(user=user, key='access_token')
        mock_user.return_value = user
        mock_token.return_value = token

        payload = {
            'username': 'hello',
            'password': 'hello',
        }
        res = self.post(self.base_url, data=payload)
        self.assertEqual(res.status_code, 201)
        self.assertIn(token.key, str(res.content))

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
