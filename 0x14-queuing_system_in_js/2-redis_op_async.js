/* Task (2) - connects to a local redis client
* Displays a message on connect and disconnect using node-redis client class
* setNewSchool() -> stores a school in redis
* displaySchoolValue() -> finds and displays a stored school (EDIT - with promisify now )
*/
import { createClient, print } from 'redis';
const { promisify } = require("util");

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
  client.set(schoolName, value, print); // print === redis.print refer to import
}

async function displaySchoolValue(schoolName) {
  // displaySchoolValue() -> finds and displays a stored 
  const clientGetPromise = promisify(client.get).bind(client);
  const value = await clientGetPromise(schoolName);
  console.log(value);
}

// (TEST) ===

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
