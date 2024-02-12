#!/usr/bin/node

const args = process.argv;

console.log(+args[2] ? 'My number: ' + +args[2] : 'Not a number');
