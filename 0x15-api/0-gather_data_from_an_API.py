#!/usr/bin/python3
# script to gather data from an API
import sys
import requests


url_usr = 'https://jsonplaceholder.typicode.com/users/'

response_usr = requests.get("{}{}".format(url_usr, sys.argv[1]), verify=False)
json_dict = response_usr.json()
name = json_dict['name']

url_todos = '{}{}/todos'.format(url_usr, sys.argv[1])
todos_list = requests.get(url_todos, verify=False).json()

total = len(todos_list)

count = 0
done_str = ""

for todo in todos_list:
    if todo['completed'] is True:
        count += 1
        done_str += "\t{}\n".format(todo['title'])

print("Employee {} is done with tasks({}/{}):".format(name, count, total))
print(done_str)
