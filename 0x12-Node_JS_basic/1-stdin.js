#!/bin/env node
var readline = require('readline');

var rl = readline.createInterface(
      process.stdin, process.stdout);

rl.setPrompt(`Welcome to Holberton School, what is your name?\n`);
rl.prompt();
rl.on('line', (name) => {
  console.log(`Your name is: ${name}`);
  rl.close();
  console.log(`This important software is now closing\n`);
});
