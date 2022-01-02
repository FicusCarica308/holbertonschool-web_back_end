// Advanced Task(100): Weak link data structure

export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let getCount;

  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 1);
  } else {
    getCount = weakMap.get(endpoint) + 1;
    if (getCount >= 5) throw new Error('Endpoint load is high');
    weakMap.set(endpoint, getCount);
  }
  return (getCount);
}
