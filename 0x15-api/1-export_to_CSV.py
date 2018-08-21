#!/usr/bin/python3
# script to gather todo data from an API and write to CSV file
import csv
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

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([user_id, uname, todo['completed'], todo['title']])
