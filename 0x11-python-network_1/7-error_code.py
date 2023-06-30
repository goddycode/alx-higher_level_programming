#!/usr/bin/python3
"""
This scripts accept URL & email as params, display response body utf-8, print error codes
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""
from sys import argv
import requests


if __name__ == "__main__":
    my_req = requests.get(argv[1])
    if my_req.status_code >= 400:
        print("Error code: {}".format(my_req.status_code))
    else:
        print(my_req.text)
