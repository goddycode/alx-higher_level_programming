#!/usr/bin/node

const numberofarguments = process.argv.length - 2;

if (numberofarguments === 0) {
  console.log('No argument');
} else if (numberofarguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
