#!/usr/bin/node

const myFile = process.argv[2];
const myText = process.argv[3];
const fs = require('fs');
fs.writeFile(myFile, myText, 'utf8', function (myError) {
if (myError) {
    console.log(myError);
  }
});
