#!/usr/bin/python3
"""
This script takes URL as parameter, fetch URL and display value from reponse header usage: ./1-hbtn_header https://intranet.hbtn.io
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    my_req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(my_req) as response:
        print(response.getheader('X-Request-Id'))
