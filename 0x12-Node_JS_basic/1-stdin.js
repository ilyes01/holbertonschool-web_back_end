// Import the built-in readline module
const readline = require('readline');

// Create an interface to read from stdin
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Display welcome message and prompt for name
console.log('Welcome to Holberton School, what is your name?');
rl.prompt();

// Handle user input
rl.on('line', (name) => {
  // Display user's name and close the program
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.exit(0);
});
