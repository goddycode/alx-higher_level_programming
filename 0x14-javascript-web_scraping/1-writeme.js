#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', function (error) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Content written to the file successfully.');
  }
});
