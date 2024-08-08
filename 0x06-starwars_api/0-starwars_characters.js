#!/usr/bin/node

const request = require('request');

// Validate command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Fetch movie data
request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (err, res, body) {
  if (err) {
    console.error('Error fetching movie data:', err);
    process.exit(1);
  }

  const characterUrls = JSON.parse(body).characters;
  fetchCharacterNames(characterUrls, 0);
});

// Function to recursively fetch and print character names
const fetchCharacterNames = (urls, index) => {
  if (index === urls.length) return;

  request(urls[index], function (err, res, body) {
    if (err) {
      console.error('Error fetching character data:', err);
      return;
    }
    console.log(JSON.parse(body).name);
    fetchCharacterNames(urls, index + 1);
  });
};
