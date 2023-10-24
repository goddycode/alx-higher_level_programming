#!/usr/bin/node

const myUrl = process.argv[2];
const request = require('request');
request(myUrl, function (myError, response) {
  if (myError) {
    console.log(myError);
  } else {
    console.log('code: ' + response.statusCode);
  }
}); 
