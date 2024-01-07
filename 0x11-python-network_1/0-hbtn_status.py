#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    d = r.json()
    print("Number of results: {}".format(d['count']))
    for i in d['results']:
        print(i['name'])
