console.log('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (n) => {
  if (n.toString().trim() !== '') {
    process.stdout.write(`Your name is: ${n.toString()}`);
  } else {
    process.exit();
  }
});
process.stdin.on('end', () => {
  console.log('This important software is now closing\n');
  process.exit();
});
