#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const contant1 = fs.readFileSync(args[2]).toString();
const contant2 = fs.readFileSync(args[3]).toString();

fs.writeFileSync(args[4], contant1 + contant2);
