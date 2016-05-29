import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        import ambry_indicator.app

        super(MyTestCase, self).setUp()

        self.app = ambry_indicator.app.app.app.test_client()

    def test_something(self):

        rv = self.app.get('/indicators/1/')
        print rv.data


if __name__ == '__main__':
    unittest.main()
