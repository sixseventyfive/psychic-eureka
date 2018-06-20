import time
import csv


class User:
    def __init__(self, id, name, goal):
        self.id = id
        self.name = name
        self.goal = goal

    def log_data(self, weight):
        with open('data/' + id + '.csv', 'a') as data:
            write = csv.writer(data)
            date = time.strftime('%d/%m/%Y')
