#!/usr/bin/node

const args = process.argv;
const fNum = +args[2];
const sNum = +args[3];

function add (a, b) {
  console.log(a + b);
}

add(fNum, sNum);
