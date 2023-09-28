#!/bin/bash

# Make a request to the specified URL
response=$(curl -s -X PUT -d "user_id=98" "http://0.0.0.0:5000/catch_me")

# Since you are not allowed to use echo or cat, we'll simply exit with the response
# The response will be displayed as the script's exit code, which can be checked

# Check if the request was successful
if [ $? -eq 0 ]; then
    exit "$response"
else
    exit 1  # Error occurred
fi

