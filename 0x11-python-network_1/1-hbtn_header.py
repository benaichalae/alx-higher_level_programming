#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
displays the value of the X-Request-Id
variable found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as request:
        info = dict(request.headers)
        content = info.get('X-Request-Id')
        print(content)
