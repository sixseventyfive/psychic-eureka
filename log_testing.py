import log
import unittest


class UserTest(unittest.TestCase):
    def setUp(self):
        self.u = log.User(1, 'test', 100)

    def test_u_attributes(self):
        self.assertEqual(self.u.id, 1)
        self.assertEqual(self.u.name, 'test')
        self.assertEqual(self.u.goal, 100)


if __name__ == '__main__':
    unittest.main()
