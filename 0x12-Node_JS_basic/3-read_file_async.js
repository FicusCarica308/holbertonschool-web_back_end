// Task (2) - using database.csv, create a function countStudents that attempts to read the
// database file synchronously

const fs = require('fs');

function countStudents(path) {
  const response = [];
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, lines) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const fields = {};
      let overallCount = 0;
      const data = lines.split('\n');
      for (const person of data) {
        if (person !== '' && data.indexOf(person) !== 0) {
          const personData = person.split(',');
          const personField = personData.slice(-1)[0];
          overallCount += 1;
          if (personField in fields) {
            fields[personField].count += 1;
            fields[personField].names.push(personData[0]);
          } else {
            fields[personField] = { count: 1, names: [personData[0]] };
          }
        }
      }
      response.push(`Number of students: ${overallCount}`);
      for (const key in fields) {
        if (key in fields) {
          response.push(`Number of students in ${key}: ${fields[key].count}. List: ${fields[key].names.join(', ')}`);
        }
      }
      console.log(`${response.join('\n')}`);
      resolve(response);
    });
  });
}

module.exports = countStudents;
