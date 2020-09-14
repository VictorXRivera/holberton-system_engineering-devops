#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_name = sys.argv[1]

    name = requests.get(url + "users/" + employee_name)
    name = name.json()

    tasks = requests.get(url + "todos?userId=" + employee_name)
    tasks = tasks.json()

    done_list = []
    for item in tasks:
        if item.get('completed') is True:
            done_list.append(item)

    done_tasks = len(done_list)
    total_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        name.get('name'), done_tasks, total_tasks))
    for item in done_list:
        print("\t {}".format(item.get('title')))
