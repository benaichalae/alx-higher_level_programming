#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
[ "$#" -eq 2 ] && jq . "$2" && curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
