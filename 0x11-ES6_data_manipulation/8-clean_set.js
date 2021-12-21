/*
  Task(8): a function named cleanSet that returns a string of all
  the set values that start with a specific string (startString).
*/
export default function hasValuesFromArray(set, startString) {
  if (startString === '') return ('');
  const editedStrings = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      editedStrings.push(value.slice(startString.length));
    }
  });

  return editedStrings.join('-');
}
