/* Task (4) - connects to a local redis client
* creates a hash table and prints it after creation
*/
import { createClient, print } from 'redis';

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

// HASH SETTING OPERATIONS ===

client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

client.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
})
