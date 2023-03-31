#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve this challenge"""

import requests
import sys

# Get the repository name and owner name from command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Make a GET request to the GitHub API to retrieve information about the repository
response = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}")

# Check the status code of the response to see if the request was successful
if response.status_code == 200:
    # If the request was successful, print some information about the repository
    repo_info = response.json()
    print(f"Repository name: {repo_info['name']}")
    print(f"Owner name: {repo_info['owner']['login']}")
    print(f"Description: {repo_info['description']}")
    print(f"Number of stars: {repo_info['stargazers_count']}")
    print(f"Number of forks: {repo_info['forks_count']}")
else:
    # If the request was not successful, print an error message
    print(f"Error: Could not retrieve information about {owner_name}/{repo_name}")

