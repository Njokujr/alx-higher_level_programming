#!/usr/bin/python3
"""
A Script that fetches the status of
url: https://alx-intranet.hbtn.io/status
"""

import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()

    print('Body Response:')
    print('\t- type: {}'.format(type(the_page)))
    print('\t- content: {}'.format(the_page))
    print('\t- utf8 content: {}'.format(the_page.decode('utf-8')))
