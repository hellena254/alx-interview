#!/usr/bin/node

const fetch = require('node-fetch');

// get the movie id from cmd
const movieId = process.argv[2];

// URL for the star wars api
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// fetch movie data from API
fetch(apiUrl)
  .then(response => response.json())
  .then(movie => {
    // check if char exists
    if (!movie.characters) {
      console.error('No character found.');
      process.exit(1);
    }

    // fetch and print character names
    const charPromises = movie.characters.map(charUrl =>
      fetch(charUrl).then(response => response.json()).then(character => console.log(character.name))
    );

    // wait for all char requests to complete
    return Promise.all(charPromises);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
    process.exit(1);
  });
