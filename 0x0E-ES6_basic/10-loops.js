export default function appendToEachArrayValue(array, appendString) {
  let return_array = []
  for (let idx of array) {
    const value = idx;
    return_array.push(appendString + value);
  }

  return return_array;
}
