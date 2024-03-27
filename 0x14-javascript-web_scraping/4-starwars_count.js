#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  let num = 0;
  const movies = JSON.parse(body).results;
  movies.forEach(element => {
    console.log(element.characters);
    if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      num++;
    }
  });
  console.log(err || num);
});
