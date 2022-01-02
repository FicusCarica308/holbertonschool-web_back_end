// Task (2) - using database.csv, create a function countStudents that attempts to read the
// database file synchronously

const fs = require('fs');

function countStudents(path) {
  const CSdata = {
    count: 0,
    names: [],
  };

  const SWEdata = {
    count: 0,
    names: [],
  };

  let overallCount = 0;

  let data;

  try {
    data = fs.readFileSync(path, 'utf8').split('\n');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  for (const item of data) {
    if (item !== '') {
      const itemData = item.split(',');
      overallCount += 1;
      if (itemData.slice(-1)[0] === 'CS') {
        CSdata.count += 1;
        CSdata.names.push(itemData[0]);
      } else {
        SWEdata.count += 1;
        SWEdata.names.push(itemData[0]);
      }
    }
  }
  console.log(`Number of students: ${overallCount}`);
  console.log(`Number of students in CS: ${CSdata.count}. List: ${CSdata.names.join(', ')}`);
  console.log(`Number of students in SWE: ${SWEdata.count}. List: ${SWEdata.names.join(', ')}`);
}

module.exports = countStudents;
