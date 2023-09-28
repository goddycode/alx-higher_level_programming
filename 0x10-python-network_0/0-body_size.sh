#!/bin/bash
# Script which takes in a URL, sends a request to
# that URL, and displays the size of the body of the response size of body
# of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
