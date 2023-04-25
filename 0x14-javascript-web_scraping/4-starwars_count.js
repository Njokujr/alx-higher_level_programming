#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movies = JSON.parse(body).results;
  const numMoviesWithWedgeAntilles = movies.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  ).length;

  console.log(numMoviesWithWedgeAntilles);
});

