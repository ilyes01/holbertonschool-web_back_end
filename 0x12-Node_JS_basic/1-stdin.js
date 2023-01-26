const readline = require('readline');

console.log('Welcome to Holberton School, what is your name?');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (name) => {
  console.log(`Your name is: ${name}`);
  rl.close();
});

process.on('exit', () => {
  console.log('This important software is now closing');
});

