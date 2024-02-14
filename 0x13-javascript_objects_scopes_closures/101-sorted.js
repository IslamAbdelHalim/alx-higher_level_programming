#!/usr/bin/node

const dict = require('./101-data').dict;
// create new object
const newDict = {};

// convert every keys and values to array
const arr = Object.keys(dict);
const arr2 = Object.values(dict);

/*
  check if the kay is present in new object 
  if present add its value to the array
  if not create a new key and create the array in this key
*/

for (let i = 0; i < arr.length; i++) {
  if (!newDict[arr2[i]]) {
    newDict[arr2[i]] = new Array(arr[i]);
  } else {
    newDict[arr2[i]].push(arr[i]);
  }
}

console.log(newDict);
