// Task(3): a function getStudentIdsSum that returns the sum of all the student ids.

export default function getStudentIdsSum(students) {
  /* if (students instanceof Array === false) {
    return [];
  } */
  return (students.reduce((prev, curr) => prev + curr.id, 0));
}
