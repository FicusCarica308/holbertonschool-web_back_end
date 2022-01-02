/*
  Task(7): a function named hasValuesFromArray that returns a boolean
  if all the elements in the array exist within the set.
*/
export default function hasValuesFromArray(set, array) {
  const setArray = Array.from(set);
  for (const item of array) {
    const result = setArray.includes(item);
    if (result === false) return (false);
  }
  return (true);
}
