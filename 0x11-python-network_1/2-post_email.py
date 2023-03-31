#!/usr/bin/python3
"""A Python Script that takes in a URL and Email, sends a POST request
to the passed URL"""

import urllib.request
import sys

if __name__ == '__main__':
    url, email = sys.argv[1:]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        res = response.read().decode('utf-8')
        print(res)
