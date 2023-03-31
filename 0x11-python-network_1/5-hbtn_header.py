#!/usr/bin/python3
"""
A Python Script that takes/sends a request to the URL and displays
the value of the variable X-Request-Id in the response header"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1:]
    r = requests.get(url)
    res = r.headers.get('X-Request-Id')
    print(res)
