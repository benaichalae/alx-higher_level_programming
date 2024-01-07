#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
displays the value of the X-Request-Id
variable found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as r:
        info = r.info()
        content = info.get('X-Request-Id')
        print(content)
