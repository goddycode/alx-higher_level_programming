#!/usr/bin/python3
"""
This scripts accept URL & email as params, display response body utf-8
"""
from sys import argv
import requests


if __name__ == "__main__":
    my_req = requests.get(argv[1])
    if my_req.status_code >= 400:
        print("Error code: {}".format(my_req.status_code))
    else:
        print(my_req.text)
