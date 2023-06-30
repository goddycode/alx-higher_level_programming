#!/usr/bin/python3
"""
This script fetches from  https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    my_req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(my_req.text)))
    print("\t- content: {}".format(my_req.text))
