import unittest
from pathlib import Path
import time
#import os

import log


class UserTest(unittest.TestCase):
    def setUp(self):
        self.u = log.User(1, 'test', 100)

    def test_user_attributes(self):
        self.assertEqual(self.u.id, 1)
        self.assertEqual(self.u.name, 'test')
        self.assertEqual(self.u.goal, 100)

    def test_check_file_created(self):
        self.u.log_data(100, 93.2)
        path = 'data/' + str(self.u.id) + '.csv'
        path = Path(path)
        self.assertTrue(path.is_file())

    def test_check_data_written(self):
        self.u.log_data(15, 18.5)
        path = 'data/' + str(self.u.id) + '.csv'
        today = time.strftime('%Y%m%d')
        with open(path, 'rb') as f:
            f.seek(-2, 2)
            while f.read(1) != b'\n':  #why is b here?
                f.seek(-2, 1)
            last = f.readline()
            line = today.encode('utf-8') + b',' + str(
                self.u.id).encode('utf-8') + b',15,18.5\r\r\n'
            self.assertEqual(last, line)


if __name__ == '__main__':
    unittest.main()
