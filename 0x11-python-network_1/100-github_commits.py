#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve this challenge"""

import requests
import sys

api_endpoint = ("https://api.github.com/repos/{}/{}/commits"
                .format(sys.argv[2], sys.argv[1]))

# Make a request to the GitHub API
response = requests.get(api_endpoint)

# Get the most recent 10 commits
commits = response.json()[:10]

# Print each commit's SHA and author name
for commit in commits:
    print("{}: {}".format(commit['sha'], commit['commit']['author']['name']))
