#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve this challenge"""

import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]
response = requests.get(f"https: // api.github.com/repos
                        / {owner_name}/{repo_name}")

if response.status_code == 200:
    repo_info = response.json()
    print(f"Repository name: {repo_info['name']}")
    print(f"Owner name: {repo_info['owner']['login']}")
    print(f"Description: {repo_info['description']}")
    print(f"Number of stars: {repo_info['stargazers_count']}")
    print(f"Number of forks: {repo_info['forks_count']}")
else:
    print(f"Error: Could not retrieve information about
          {owner_name}/{repo_name}")
