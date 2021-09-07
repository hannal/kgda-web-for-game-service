from unittest.mock import patch
from test_plus import TestCase

from accounts.models import User, AccessToken


class AuthenticateTest(TestCase):
    base_url = '/accounts/'
    auth_url = f'{base_url}auth/'
    me_url = f'{base_url}me/'

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
        res = self.post(self.auth_url, data=payload)
        self.assertEqual(res.status_code, 201)
        data = res.json()
        self.assertEqual(token.key, data['access_token'])

    @patch('accounts.models.User.find_by_credentials')
    def test_auth_failure(self, mock):
        mock.return_value = None

        res = self.get(self.auth_url)
        self.assertEqual(405, res.status_code)

        res = self.post(self.auth_url)
        self.assertEqual(400, res.status_code)

        payload = {
            'username': 'hello',
            'password': 'hello',
        }
        res = self.post(self.auth_url, data=payload)
        self.assertEqual(401, res.status_code)

    @patch('accounts.models.AccessToken.objects.get')
    def test_me_success(self, mock):
        user = User(username='authorized_user')
        token = AccessToken(user=user, key='valid_token')
        mock.return_value = token

        headers = {
            'HTTP_AUTHORIZATION': f'Token {token.key}',
        }

        res = self.get(self.me_url, extra=headers)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(user.username, data['username'])
