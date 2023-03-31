#!/usr/bin/python3
"""A Python Script that takes in a URL, sends a request to the URL
and displays the body of the response."""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code == 200:
        print(r.text)

    else:
        print('Error code: {}'.format(r.status_code))
