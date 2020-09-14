#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""


import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_name = sys.argv[1]
    filename = employee_name + ".csv"

    name = requests.get(url + "users/" + employee_name)
    name = name.json()

    tasks = requests.get(url + "todos?userId=" + employee_name)
    tasks = tasks.json()

    with open(filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for item in tasks:
            writer.writerow((item.get('userId'), name.get('username'),
                            item.get('completed'), item.get('title')))
