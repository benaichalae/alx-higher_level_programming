#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];


if (!apiUrl) {
  console.error('Please provide the Star Wars API URL as an argument.');
  process.exit(1);
}


request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results;

      // Filter films where Wedge Antilles (character ID 18) is present
      const filmsWithWedge = films.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );

      // Print the number of films with Wedge Antilles
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
