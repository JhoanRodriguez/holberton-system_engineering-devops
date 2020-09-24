#!/usr/bin/python3
"""Module Export to JSON"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    _id = argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        _id)

    req_user = requests.get(url_users).json()
    req_todo = requests.get(url_todo).json()

    data_dict = {}
    data_list = []

    for task in req_todo:
        user_task = {}
        user_task["task"] = task['title']
        user_task["completed"] = task['completed']
        user_task["username"] = req_user['username']
        data_list.append(user_task)

    data_dict[argv[1]] = data_list

    with open('{}.json'.format(_id), mode='w') as json_file:
        json.dump(data_dict, json_file)
