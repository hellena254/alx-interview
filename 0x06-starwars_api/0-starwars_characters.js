#!/usr/bin/node

const request = require('request');

// get movie id from cmd
const movieId = process.argv[2];

// URL for star wars API endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data from API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  // check if char field exists
  if (!movie.characters) {
    console.error('Characters not found in the specified movie.');
    process.exit(1);
  }

  // fetch and print char names
  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching data:', error);
	return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
