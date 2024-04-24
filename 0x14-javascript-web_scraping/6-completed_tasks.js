#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  body = JSON.parse(body);
  const completedTasks = {};

  for (let i = 0; i < body.length; i++) {
    const userId = body[i].userId;
    const completed = body[i].completed;

    if (completed && !completedTasks[userId]) {
      completedTasks[userId] = 0;
    }

    if (completed) {
      ++completedTasks[userId];
    }
  }
  console.log(completedTasks);
});
