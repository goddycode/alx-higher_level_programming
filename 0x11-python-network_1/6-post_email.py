#!/usr/bin/python3
"""
This scripts accept URL & email as params, send POST req to URL
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    my_req = requests.post(url, data=payload)
    print(my_req.text)
