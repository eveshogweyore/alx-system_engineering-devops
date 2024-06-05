#!/usr/bin/python3
""" Check the number of subscribers in a subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ Given subreddit, return number of subscribers. """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url)
   
    if response.status_code == 200:
        subreddit_data = response.json()
        return (subreddit_data['data']['subscribers'])

    return 0
