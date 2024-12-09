#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  for (const url of characterUrls) {
    await new Promise((resolve) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          resolve();
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error(`Error: Received status code ${charResponse.statusCode} for character URL ${url}`);
          resolve();
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name.trim());
        resolve();
      });
    });
  }
});
