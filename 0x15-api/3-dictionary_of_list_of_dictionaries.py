#!/usr/bin/python3
"""
Returns information about all employees' TODO list progress in JSON format
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    to_json = "todo_all_employees.json"

    employees = requests.get(url + "users/")
    employees = employees.json()

    tasks_todo = {}
    for employee in employees:
        employee_id = employee.get('id')
        tasks = requests.get(url + "todos?userId=" + str(employee_id))
        tasks = tasks.json()

        tasks_list = []
        for item in tasks:
            tasks_list.append(item)

        tasks_todo[employee_id] = tasks_list

    with open(to_json, mode="w") as json_file:
        json.dump(tasks_todo, json_file)
