#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""


import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_name = sys.argv[1]
    filename = employee_name + ".json"

    name = requests.get(url + "users/" + employee_name)
    name = name.json()

    tasks = requests.get(url + "todos?userId=" + employee_name)
    tasks = tasks.json()

    done_list = []
    for item in tasks:
        done_list.append(item)

    todo = {}
    todo[employee_name] = done_list

    with open(filename, mode="w") as json_file:
        json.dump(todo, json_file)
