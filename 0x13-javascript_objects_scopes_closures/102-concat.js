#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const contant1 = fs.readFileSync(args[2]).toString() + '\n';
const contant2 = fs.readFileSync(args[3]).toString() + '\n';

fs.writeFileSync(args[4], contant1 + contant2);