#!/usr/bin/node

const myReq = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
myReq.get(url + id, function (myError, res, body) {
  if (myError) {
    console.log(myError);
  } else {
    console.log(JSON.parse(body).title);
  }
});
