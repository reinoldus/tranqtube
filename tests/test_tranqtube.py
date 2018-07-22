import unittest

import tranqtube


class TranqtubeTestCase(unittest.TestCase):

    def setUp(self):
        self.app = tranqtube.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to tranqtube', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
