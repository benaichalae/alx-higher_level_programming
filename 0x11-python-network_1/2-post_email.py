#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    content = urllib.parse.urlencode(val).encode('ascii')
    re = urllib.request.Request(argv[1], data=content, method='POST')
    with urllib.request.urlopen(re) as r:
        readed = r.read().decode('utf-8')
        print(readed)
