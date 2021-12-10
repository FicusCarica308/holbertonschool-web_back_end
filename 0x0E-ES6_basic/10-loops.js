export default function appendToEachArrayValue(array, appendString) {
  const returnArray = [];
  for (const idx of array) {
    const value = idx;
    returnArray.push(appendString + value);
  }

  return returnArray;
}
