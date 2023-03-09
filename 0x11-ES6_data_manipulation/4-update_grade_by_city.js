export default function getStudentIdsSum(students) {
  let sum = 0;
  if (Array.isArray(students)) {
    for (let i = 0; i < students.length; i += 1) { // use i += 1 instead of i++
      sum += students[i].id;
    }
  }
  return sum;
}
