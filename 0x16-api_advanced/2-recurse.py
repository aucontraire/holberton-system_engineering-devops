#!/usr/bin/python3
"""Function that prints top ten hot posts for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Gets hot posts in subreddit
       Args:
           subreddit (str): name of subreddit
           hot_list (list): list of titles
           after (str): id of next set of results
    """
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?after={}'.format(
            base_url,
            subreddit, after), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        hot_dict = response.json()
        if len(hot_dict['data']['children']) == 0:
            return hot_list
        else:
            for d in hot_dict['data']['children']:
                hot_list.append(d['data']['title'])

            after = hot_dict['data']['after']
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after=after)
