#!/bin/bash
# Script which makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -s -X PUT -L -d "user_id=98" -H "You got me!" 0.0.0.0:5000/catch_me
