#!/usr/bin/node

const args = process.argv;
const len = args.length;

if (len <= 2) {
  console.log('No Argument');
} else {
  console.log('Arguments found');
}
