#!/usr/bin/python3
"""
This scripts accepts URL as parameter, fetch URL and display value
"""
from sys import argv
import requests


if __name__ == "__main__":
    my_req = requests.get(argv[1])
    print(my_req.headers.get('X-Request-Id'))
