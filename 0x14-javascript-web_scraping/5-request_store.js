#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(args[1], body, function (error, response) {
      if (error) console.log('error', error);
    });
  }
});
