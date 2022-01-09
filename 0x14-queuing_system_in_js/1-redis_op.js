/* Task (1) - connects to a local redis client
* Displays a message on connect and disconnect using node-redis client class
* setNewSchool() -> stores a school in redis
* displaySchoolValue() -> finds and displays a stored school
*/
import { createClient } from 'redis';

// (REDIS CLIENT) ===

const client = createClient();

client.on('connect', () => {
  // Displays on redis connection
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  // Displays if redis connection fails
  console.log(`Redis client not connected to the server: ${err}`);
});

// (FUNCTIONS) ===

function setNewSchool(schoolName, value) {
  // setNewSchool() -> stores a school in redis
  client.set(schoolName, value, (err, reply) => {
    console.log(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  // displaySchoolValue() -> finds and displays a stored school
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

// (TEST) ===

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
