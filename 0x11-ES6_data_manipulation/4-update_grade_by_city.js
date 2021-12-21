/*
Task(4): a function updateStudentGradeByCity that returns an array of students
for a specific city with their new grade
*/

export default function updateStudentGradeByCity(students, city, newGrades) {
  const callBack = (student) => {
    const updatedStudent = student;
    const gradeForId = newGrades.filter((grade) => grade.studentId === student.id);
    if (gradeForId.length >= 1) {
      updatedStudent.grade = gradeForId[0].grade;
    } else {
      updatedStudent.grade = 'N/A';
    }
    return updatedStudent;
  };
  return (students.filter((student) => student.location === city).map(callBack));
}
