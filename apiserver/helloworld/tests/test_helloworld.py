from test_plus import TestCase


class HelloWorldTest(TestCase):
    def test_hello_world(self):
        res = self.get('/helloworld/')
        self.assertEqual(res.status_code, 200)
