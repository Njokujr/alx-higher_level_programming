#!/usr/bin/node
const request = require('request');

// Get the API URL from command line argument
const apiUrl = process.argv[2];

// Send a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results; // Extract the films array from the API response
      let wedgeAntillesCount = 0; // Initialize count to 0

      // Loop through the films and check if Wedge Antilles is present in each film
      for (const film of films) {
        const characters = film.characters; // Get the characters array from each film
        if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          // Check if Wedge Antilles' character ID (18) is present in the characters array
          wedgeAntillesCount++;
        }
      }

      console.log('Number of movies where Wedge Antilles is present:', wedgeAntillesCount);
    } catch (error) {
      console.error(error);
    }
  }
});
