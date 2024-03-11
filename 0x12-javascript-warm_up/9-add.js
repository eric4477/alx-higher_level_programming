#!/usr/bin/node
// sum two integer arguments

const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add(a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(firstArg, secondArg);
