#!/bin/env node
var readline = require('readline');

var rl = readline.createInterface(
        process.stdin, process.stdout);

rl.setPrompt(`What is your name?\n`);
rl.prompt();
rl.on('line', (name) => {
    console.log(`Your name is: ${name}`);
    rl.close();
});
