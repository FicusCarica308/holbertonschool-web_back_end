// Task (5) - a small more complex HTTP server using the http module

const http = require('http');
const countStudents = require('./3-read_file_async.js')

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
    countStudents(database)
    .then((students) => {
        res.end('This is the list of our students\n' + `${students.join('\n')}`);
    })
        .catch((error) => {
        console.log(error);
    });

  }
});

app.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}/`);
});

module.exports = app;
