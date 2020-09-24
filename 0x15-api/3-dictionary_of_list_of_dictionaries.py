#!/usr/bin/python3
"""Module export all to Dictionary of list"""

import json
import requests


if __name__ == '__main__':
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todo = 'https://jsonplaceholder.typicode.com/todos'

    req_user = requests.get(url_users).json()
    req_todo = requests.get(url_todo).json()

    data_dict = {}
    for user in req_user:
        _users = []

        for task in req_todo:
            if user['id'] == task['userId']:
                user_task = {}
                user_task["task"] = task['title']
                user_task["completed"] = task['completed']
                user_task["username"] = user['username']
                _users.append(user_task)

        data_dict[user['id']] = _users

    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(data_dict, json_file)
