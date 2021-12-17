// Task(2): Implement a class named HolbertonCourse.

export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Name getter and setter
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // Length getter and setter
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  // Students getter and setter
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (newStudents instanceof Array) {
      this._students = newStudents;
    } else {
      throw new TypeError('Students must be an Array');
    }
  }
}
