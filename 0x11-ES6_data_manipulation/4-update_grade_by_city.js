export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }
  const updatedStudents = students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.find((grade) => grade.studentId === student.id);
    return grade !== undefined ? { ...student, grade: grade.grade } : { ...student, grade: 'N/A' };
  });
  return updatedStudents.length > 0 ? updatedStudents : 0;
}
