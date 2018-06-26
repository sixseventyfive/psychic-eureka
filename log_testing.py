import unittest
import sqlite3
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

    def test_check_db_created(self):
        log.database('db_init.sql', True)
        path = 'data/db'
        path = Path(path)
        self.assertTrue(path.is_file())

    def test_check_tbl_exist(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';"
        tables = ['users', 'goal', 'track']
        for tbl in tables:
            exists, msg = log.database(sql.format(tbl), False)
            self.assertEqual(exists[0], (tbl, )) #had to make tbl a tuple



if __name__ == '__main__':
    unittest.main()
