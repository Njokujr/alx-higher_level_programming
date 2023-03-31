#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve this challenge"""

import requests
import sys

# Get repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Construct URL for GitHub API
url = f"https://api.github.com/repos/{owner_name}/{repo_name}"

# Send GET request to GitHub API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Get repository information from response
    repo_info = response.json()
    # Print repository name, description, and number of stars
    print(f"Repository Name: {repo_info['name']}")
    print(f"Description: {repo_info['description']}")
    print(f"Number of Stars: {repo_info['stargazers_count']}")
else:
    # Print error message
    print(f"Error: {response.status_code}")
