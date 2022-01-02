// Task(6): a function named setFromArray that returns a Set from an array
export default function setFromArray(array) {
  const set1 = new Set();
  for (const item of array) {
    set1.add(item);
  }
  return (set1);
}
