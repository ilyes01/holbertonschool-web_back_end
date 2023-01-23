const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

console.log('Welcome to Holberton School, what is your name?');

rl.question('', (name) => {
    console.log(`Your name is: ${name}`);
    rl.close();
});

rl.on("close", () => {
    console.log("This important software is now closing");
    process.exit(0);
});

