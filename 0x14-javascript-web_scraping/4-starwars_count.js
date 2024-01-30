#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results;
      const filmsWithWedge = films.filter((film) =>
        film.characters.includes('18')
      );
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
