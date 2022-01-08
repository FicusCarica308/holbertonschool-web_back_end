// Task (5) - a small more complex HTTP server using the http module

const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv.slice(2)[0];

const host = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(database)
      .then((students) => {
        res.end(`${students.join('\n')}`);
      })
      .catch((error) => {
        res.end(error.message);
      });
  }
});

app.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}/`);
});

module.exports = app;
