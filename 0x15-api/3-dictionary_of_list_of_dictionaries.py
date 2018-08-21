#!/usr/bin/python3
# script to gather all todo data from an API and write to JSON file
import json
import requests
import sys


def get_username(base_url, user_id):
    """Gets username
       Args:
           base_url (str): base url for API
           user_id (str): user id number
       Returns: username
    """
    response = requests.get(
        "{}users/{}".format(base_url, user_id), verify=False)
    usr_dict = response.json()
    return usr_dict['username']


def get_complete_todo_list(base_url):
    """Gets complete todo list
       Args:
           base_url (str): base url for API
       Returns: list of todo items (dicts)
    """
    response = requests.get(
        "{}todos".format(base_url), verify=False)
    return response.json()


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_dict = {}
    todo_dict = {}
    todo_list = get_complete_todo_list(base_url)

    with open('todo_all_employees.json', 'w') as f:
        uname = None
        for task in todo_list:
            user_id = str(task['userId'])
            if user_id in users_dict.keys():
                uname = users_dict[user_id]
            else:
                uname = get_username(base_url, user_id)
                users_dict[user_id] = uname
                todo_dict[user_id] = []

            todo = {}
            todo['task'] = task['title']
            todo['completed'] = task['completed']
            todo['username'] = uname
            todo_dict[user_id].append(todo)

        f.write(json.dumps(todo_dict))
