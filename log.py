import time
import sqlite3


class User:
    def __init__(self, id, name, goal):
        self.id = id
        self.name = name
        self.goal = goal
        self.data = 'data/' + str(self.id) + '.csv'

    def log_data(self, weight, pcent):
        bmi = weight / (height**2)
        row = {'id': self.id, 'weight': weight, 'pcent': pcent, 'bmi': bmi}


def database(sql, script_flag):
    db = sqlite3.connect('data/db')
    cursor = db.cursor()
    if script_flag == True:
        try:
            cursor.executescript(sql)
        except:
            print('Error with sql script')
    else:
        try:
            cursor.execute(sql)
        except:
            print('Error with sql command')
    try:
        results = cursor.fetchall()
    except:
        results = 'No reults to retreive'
    try:
        db.commit()
        msg = 'SQL changes written'
    except:
        msg = 'SQL not commited'
    db.close()
    return results, msg


if __name__ == '__main__':
    with open('db_init.sql', 'r') as tbl_init:
        database(tbl_init, True)
    uid = input('Please enter your user ID:\n')
    uid_valid = 'SELECT COUNT(*) FROM users WHERE user_id = {}'.format(uid)
    uid_valid, msg = database(uid_valid, False)
    try:
        uid_valid[0]
    except IndexError:
        print('create new user')
#    if uid_valid[0] == 1:
#        pass
#    else:
#        #create_new_user()
#        pass
