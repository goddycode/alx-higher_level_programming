#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log('Error:', err);
  } else if (response.statusCode === 200) {
    const completedTasksByUser = {};

    try {
      const tasks = JSON.parse(body);

      for (const task of tasks) {
        if (task.completed === true) {
          if (completedTasksByUser[task.userId] === undefined) {
            completedTasksByUser[task.userId] = 1;
          } else {
            completedTasksByUser[task.userId]++;
          }
        }
      }
      console.log(completedTasksByUser);
    } catch (error) {
      console.log('Error parsing JSON data:', error.message);
    }
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});

