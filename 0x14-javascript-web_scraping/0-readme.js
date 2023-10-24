#!/usr/bin/node

const myFile = process.argv[2];
const fs = require('fs');
fs.readFile(myFile, 'utf8', function (myError, myData) {
  if (myError) {
    console.log(myError);
  } else {
    console.log(myData);
  }
});
