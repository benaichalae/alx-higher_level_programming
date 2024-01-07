#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    result = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(result.json()['id'])
    except KeyError:
        print("None")
