// Task(0): Edit a set of given functions
export function taskFirst() {
  // changed from var
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  // changed from var
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
