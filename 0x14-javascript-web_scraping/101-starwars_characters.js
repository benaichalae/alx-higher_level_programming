#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    function getCharacterName(characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else if (charResponse.statusCode !== 200) {
            reject(`Invalid status code: ${charResponse.statusCode}`);
          } else {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          }
        });
      });
    }

    Promise.all(characters.map(getCharacterName))
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error('Error:', err));
  }
});
