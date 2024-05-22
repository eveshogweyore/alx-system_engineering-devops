#!/usr/bin/python3
""" First use of REST API. """

import json
import requests
from sys import argv

if __name__ == "__main__":
    users_url = f"https://jsonplaceholder.typicode.com/users/"
    users = requests.get(users_url)
    all_users = users.json()
    total_users = len(all_users)

    i = 1
    final_dict = {}

    while i <= total_users:
        todos_url = f"https://jsonplaceholder.typicode.com/users/{i}/todos"
        user_url = f"https://jsonplaceholder.typicode.com/users/{i}"

        todos = requests.get(todos_url)
        user = requests.get(user_url)

        todos = todos.json()
        user = user.json()

        for todo in todos:
            del todo['userId']
            del todo['id']
            todo['task'] = todo['title']
            todo['username'] = user['username']
            del todo['title']

        key = f"{user['id']}"
        value = todos

        final_dict[key] = value

        i += 1

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as f:
        json.dump(final_dict, f)
