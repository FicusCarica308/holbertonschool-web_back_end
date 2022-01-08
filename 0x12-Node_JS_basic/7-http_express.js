// Task(6) - small express app

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const database = process.argv.slice(2)[0];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(database)
    .then((students) => {
      res.end(`${students.join('\n')}`);
    })
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
