from test_plus import TestCase


class AuthenticateTest(TestCase):
    base_url = '/accounts/auth/'

    def test_auth_success(self):
        payload = {
            'username': 'hello',
            'password': 'hello',
        }
        res = self.post(self.base_url, data=payload)
        self.assertEqual(res.status_code, 200)
