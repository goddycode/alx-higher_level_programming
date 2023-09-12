#!/usr/bin/node

const MyArg = parseInt(process.argv[2], 10);

if (isNaN(MyArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${MyArg}`);
}
