#!/bin/bash
# Script which makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with corresponded message
curl -s -X PUT -L -d "user_id=98" -H "You got me!" 0.0.0.0:5000/catch_me