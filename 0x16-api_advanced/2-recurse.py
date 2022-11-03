#!/usr/bin/python3
"""A function that requests all of the hot_list articles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function that requests all of the hot_list articles of a subreddit"""

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100}
    headers = {'User-Agent': ''}
    if after:
        params['after'] = after
    r = requests.get(URL, headers=headers, params=params)
    if (r.status_code is not 200 and after is None):
        return(None)
    r = r.json()
    posts = r['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    if r['data']['after']:
        return(recurse(subreddit, hot_list, after=r['data']['after']))
    else:
        return(hot_list)
