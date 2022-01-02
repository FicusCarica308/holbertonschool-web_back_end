// Task (2) - using database.csv, create a function countStudents that attempts to read the
// database file synchronously

const fs = require('fs');

function countStudents(path) {
  const fields = {};
  let overallCount = 0;
  let data;

  try {
    data = fs.readFileSync(path, 'utf8').split('\n');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  for (const person of data) {
    if (person !== '') {
      person.trim();
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
  console.log(`Number of students: ${overallCount}`);
  for (const key in fields) {
    if (key in fields) {
      console.log(`Number of students in ${key}: ${fields[key].count}. List: ${fields[key].names.join(', ')}`.trim());
    }
  }
}

module.exports = countStudents;
