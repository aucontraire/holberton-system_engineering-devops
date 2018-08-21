#!/usr/bin/python3
# script to gather todo data from an API and write to JSON file
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
        "{}users/{}".format(base_url, user_id))
    usr_dict = response.json()
    return usr_dict['username']


def get_todo_list(base_url, user_id):
    """Gets todo list
       Args:
           base_url (str): base url for API
           user_id (str): user id number
       Returns: list of todo items (dicts)
    """
    response = requests.get(
        "{}users/{}/todos".format(base_url, user_id))
    return response.json()


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    uname = get_username(base_url, user_id)
    todo_list = get_todo_list(base_url, user_id)

    with open('{}.json'.format(user_id), 'w') as f:
        todo_dict = {}
        todo_dict[sys.argv[1]] = []
        for todo in todo_list:
            task = {}
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['username'] = uname
            todo_dict[sys.argv[1]].append(task)

        f.write(json.dumps(todo_dict))
