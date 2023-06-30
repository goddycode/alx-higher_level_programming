#!/bin/bash
# Script which makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with corresponded message
curl -s -o response.txt 0.0.0.0:5000/catch_me
