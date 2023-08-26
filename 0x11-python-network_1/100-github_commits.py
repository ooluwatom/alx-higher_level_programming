#!/usr/bin/python3
"""Script to request commits via the GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    repository = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/\
commits?per_page=10'.format(owner, repository)

    r = requests.get(url)

    r = r.json()

    for commit in r:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
