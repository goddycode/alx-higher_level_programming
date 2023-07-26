#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi.dev/api/';

function fetchMovieCharacters(movieId) {
  const movieUrl = `${apiUrl}films/${movieId}/`;

  request(movieUrl, function (err, response, body) {
    if (err) {
      console.log('Error:', err);
    } else if (response.statusCode === 200) {
      try {
        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        fetchCharactersData(characterUrls);
      } catch (error) {
        console.log('Error parsing movie data:', error.message);
      }
    } else {
      console.log('An error occurred. Status code:', response.statusCode);
    }
  });
}

function fetchCharactersData(characterUrls) {
  for (const characterUrl of characterUrls) {
    request(characterUrl, function (err, response, body) {
      if (err) {
        console.log('Error:', err);
      } else if (response.statusCode === 200) {
        try {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } catch (error) {
          console.log('Error parsing character data:', error.message);
        }
      } else {
        console.log('An error occurred. Status code:', response.statusCode);
      }
    });
  }
}

const movieId = process.argv[2];
if (!movieId) {
  console.log('Please provide a movie ID as the first argument.');
} else {
  fetchMovieCharacters(movieId);
}

