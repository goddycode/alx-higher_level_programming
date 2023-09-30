#!/usr/bin/python3
import requests
import sys

'''task 5 script'''

if __name__ == '__main__':

    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
