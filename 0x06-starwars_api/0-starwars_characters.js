#!/usr/bin/node

const request = require('request');

// Check for Movie ID argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Fetch movie data
request('https://swapi-api.hbtn.io/api/films/' + movieId, function (err, res, body) {
  if (err) {
    console.error('Error fetching movie data:', err);
    process.exit(1);
  }

  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

// Recursive function to fetch character names
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) {
      console.error('Error fetching character data:', err);
      return;
    }
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
