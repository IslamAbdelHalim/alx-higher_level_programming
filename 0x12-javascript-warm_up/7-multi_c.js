#!/usr/bin/node

const args = process.argv;
const x = args[2];

if (x) {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}