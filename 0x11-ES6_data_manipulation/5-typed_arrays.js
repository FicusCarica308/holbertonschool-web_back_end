/*
Task(5): a function named createInt8TypedArray that returns a new
ArrayBuffer with an Int8 value at a specific position.
*/

export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const viewer = new DataView(buffer);
  try {
    viewer.setUint8(position, value);
  } catch (RangeError) {
    throw new Error('Position outside range');
  }
  return (viewer);
}
