// Task(1): a function named initializeRooms. It should return an array of 3 ClassRoom objects

import ClassRoom from './0-classroom';

export default function initializeRooms() {
  return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
}
