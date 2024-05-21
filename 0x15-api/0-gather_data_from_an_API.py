#!/usr/bin/python3
""" First use of REST API. """

import requests
from sys import argv

if __name__ == "__main__":
    todos_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/"

    todos = requests.get(todos_url)
    users = requests.get(users_url)

    response_todos = todos.json()
    response_users = users.json()

    refined_todos = []

    for record in response_todos:
        if record["completed"]:
            refined_todos.append(record)

    for emp in response_users:
        if emp["id"] == int(argv[1]):
            emp_name = emp["name"]
            break

    a = len(refined_todos)
    b = len(response_todos)

    print(f"Employee {emp_name} is done with tasks ({a}/{b})")
    for record in refined_todos:
        print(f"\t {record['title']}")
