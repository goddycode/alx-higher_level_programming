#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(myUrl, function (myError, response, body) {
  if (!myError) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (myError, response, body) {
        if (!myError) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
