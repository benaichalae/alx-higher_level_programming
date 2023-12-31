#!/usr/bin/python3
"""
takes in a URL sends a request to the URL and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    status = requests.get(argv[1]).status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(requests.get(argv[1]).text)
