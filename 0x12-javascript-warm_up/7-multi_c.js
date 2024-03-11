#!/usr/bin/node
// printing C is fun depending on number of occurences

if (isNaN(process.argv[2])) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log("C is fun");
  }
}
