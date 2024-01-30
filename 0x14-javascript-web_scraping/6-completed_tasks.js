#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
