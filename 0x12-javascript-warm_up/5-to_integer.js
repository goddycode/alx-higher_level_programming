#!/usr/bin/node

exports.printNumber = function(arg) {
  if (!isNaN(parseInt(arg))) {
    console.log("My number:", parseInt(arg));
  } else {
    console.log("Not a number");
  }
};
