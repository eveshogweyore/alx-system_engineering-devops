#!/usr/bin/python3
""" First use of REST API. """

import requests
from sys import argv
import csv

if __name__ == "__main__":
    todos_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    todos = requests.get(todos_url)
    user = requests.get(user_url)

    r_todos = todos.json()
    r_user = user.json()

    emp_usrn = r_user['username']

    refined_data = []
    for data in r_todos:
        refined_data.append(
            [data['userId'],
             emp_usrn,
             data['completed'],
             data['title']]
        )

    csv_file = f"{argv[1]}.csv"

    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(refined_data)
