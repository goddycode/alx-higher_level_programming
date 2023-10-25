#!/usr/bin/node

const myUrl = process.argv[2];
const myFile = process.argv[3];
const fs = require('fs');
const request = require('request');
request(myUrl).pipe(fs.createWriteStream(myFile));
