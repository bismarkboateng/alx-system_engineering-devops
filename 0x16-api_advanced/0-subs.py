#!/usr/bin/python3
"""
A function that queries the Reddit API and
returns the number of subscribersfor a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """A Function that gets the number of subscribers for a subreddit"""

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': ''}

    r = requests.get(URL, headers=headers)
    if (r.status_code != 200):
        return (0)
    r = r.json()
