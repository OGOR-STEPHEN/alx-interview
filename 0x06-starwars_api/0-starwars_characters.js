#!/usr/bin/env node
const request = require('request');

const getMovieCharacters = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      movieData.characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
};

if (require.main === module) {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
