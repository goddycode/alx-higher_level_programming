#!/usr/bin/node

const re = require('re');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const executed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.executed === true) {
        if (executed[task.userId] === undefined) {
          executed[task.userId] = 1;
        } else {
          executed[task.userId]++;
        }
      }
    }
    console.log(executed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
