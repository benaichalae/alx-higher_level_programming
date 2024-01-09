#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/"+ owner + "/" + repo_name +"/commits/"

    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
