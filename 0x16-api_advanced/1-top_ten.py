#!/usr/bin/python3
"""function that returns the number of subscribers for a given subreddit"""
import requests


def top_ten(subreddit):
    """Gets top ten posts in subreddit
       Args:
           subreddit (str): name of subreddit
    """
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?limit=10'.format(
            base_url, subreddit), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    hot_dict = response.json()

    for d in hot_dict['data']['children']:
        print(d['data']['title'])
