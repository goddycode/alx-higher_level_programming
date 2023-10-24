#!/usr/bin/node

const myfile = process.argv[2];
const mytext = process.argv[3];
const fs = require('fs');
fs.writeFile(myfile, mytext, 'utf8', function (myerror) {
  if (myerror) {
    console.log(myerror);
  }
});
