#!/usr/bin/python3
"""
A Python Script that takes in a URL and an Email add, sends a POST request
to the passed URL with the email as a parameter, and finally displays the
body of the response."""

import requests
import sys

if __name__ == '__main__':
    url, email = sys.argv[1:]
    data = {'email': email}

    r = requests.post(url, data=data)
    print(r.text)
