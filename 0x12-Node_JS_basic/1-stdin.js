// Task(1) -  a program named 1-stdin.js that will be executed through command line using process

process.stdin.setEncoding('utf-8');

console.log('Welcome to Holberton School, what is your name?');

// waits for stdin
process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write(`Your name is: ${chunk}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing');
});
