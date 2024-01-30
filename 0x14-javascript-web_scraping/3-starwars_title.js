#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const film = JSON.parse(body);
      console.log(film.title);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
