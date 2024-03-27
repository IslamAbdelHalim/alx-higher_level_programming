#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  const tasks = JSON.parse(body);
  const userTask = {};
  tasks.forEach(element => {
    if (element.completed === true) {
      if (userTask[element.userId] === undefined) {
        userTask[element.userId] = 1;
      } else {
        userTask[element.userId] += 1;
      }
    }
  });
  console.log(err || userTask);
});
