/*
  Task(10): a function named updateUniqueItems that returns an updated map for
  all items with initial quantity at 1.
*/
export default function groceriesList(map) {
  if (map instanceof Map === false) throw new Error('Cannot process');
  map.forEach((value, key) => { if (value === 1) map.set(key, 100); });
  return (map);
}
