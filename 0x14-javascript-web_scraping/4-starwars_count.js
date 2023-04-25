#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];

// make the request to the API URL
request(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  // parse the JSON response into an object
  const data = JSON.parse(body);

  // filter the films array to only include those where Wedge Antilles appears
  const filmsWithWedge = data.results.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));

  // print the count of films with Wedge Antilles
  console.log(filmsWithWedge.length);
});
