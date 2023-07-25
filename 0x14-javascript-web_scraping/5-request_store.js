#!/usr/bin/node
const fs = require('fs');
const re = require('re');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
