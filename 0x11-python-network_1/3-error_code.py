#!/usr/bin/python3
"""A Python Script that takes in a URL sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print('Error code: {}'.format(e.code))
