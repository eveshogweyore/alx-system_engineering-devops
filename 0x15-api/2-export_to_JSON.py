#!/usr/bin/python3
""" First use of REST API. """

import json
import requests
from sys import argv

if __name__ == "__main__":
    idz = argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/users/{idz}/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{idz}"

    todos = requests.get(todos_url)
    user = requests.get(users_url)

    r_todos = todos.json()
    r_user = user.json()

    username = r_user["username"]

    for todo in r_todos:
        del todo['userId']
        del todo['id']
        todo['task'] = todo['title']
        todo['username'] = username
        del todo['title']

    final_todos = {}
    final_todos[idz] = r_todos

    json_file = f"{idz}.json"
    with open(json_file, 'w') as f:
        json.dump(final_todos, f)
