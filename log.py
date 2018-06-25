import time
import csv


class User:
    def __init__(self, id, name, goal):
        self.id = id
        self.name = name
        self.goal = goal
        self.data = 'data/' + str(self.id) + '.csv'

    def log_data(self, weight, pcent):
        with open(self.data, 'a') as data:
            write = csv.writer(data)
            date = time.strftime('%Y%m%d')
            write.writerow([date, self.id, weight, pcent])


if __name__ == '__main__':
    print('hi, you know what to do, so do the thing that you are supposed to')
    name = input('name?\n')
    goal = input('goal?\n')
    weight = input('weight?\n')
    pcent = input('percentage? (optional)\n')
    if name == 'jo' or name == 'Jo':
        user = User(1, name, goal)
    elif name == 'Callan' or name == 'callan':
        user = User(2, name, goal)
    user.log_data(weight, pcent)
