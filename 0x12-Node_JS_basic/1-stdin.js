process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const inpt = process.stdin.read();
  if (inpt !== "") {
    process.stdout.write(`Your name is: ${inpt}`);
  }
});
process.on('exit', () => {
  process.stdout.write('This important software is now closing\n');
});
