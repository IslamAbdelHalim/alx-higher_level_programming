#!/usr/bin/node

const myArray = require('./100-data').list;

console.log(myArray);

const newArray = myArray.map((x, idx) => x * idx);

console.log(newArray);
