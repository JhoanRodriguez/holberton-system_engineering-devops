#!/usr/bin/python3
"""Module Export to CSV"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    _id = argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        _id)

    req_user = requests.get(url_users).json()
    req_todo = requests.get(url_todo).json()

    with open('{}.csv'.format(_id), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quoting=csv.QUOTE_ALL)
        for task in req_todo:
            csv_writer.writerow([task['userId'], req_user['username'],
                                 task['completed'], task['title']])
