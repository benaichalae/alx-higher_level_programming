#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let occurance = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        occurance = occurance + 1;
      }
    }
  }
  console.log(occurance);
});
