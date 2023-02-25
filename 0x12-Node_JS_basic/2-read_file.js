const fs = require('fs');

function countStudents(path) {
  try {
    const dataTxt = fs.readFileSync(path, { encoding: 'utf8' }).split(/\r?\n/);
    const data = [];
    for (const line of dataTxt) {
      if (line.trim()) {
        data.push(line.split(','));
      }
    }
    const firstNameIndex = data[0].indexOf('firstName');
    const subjectIndex = data[0].indexOf('subject');
    const studentsBySubject = {};
    for (const line of data.slice(1)) {
      const [firstName, lastName, age, city, subject] = line;
      if (subject in studentsBySubject) {
        studentsBySubject[subject].push(`${firstName} ${lastName}`);
      } else {
        studentsBySubject[subject] = [`${firstName} ${lastName}`];
      }
    }
    console.log(`Number of students: ${data.length - 1}`);
    for (const [subject, students] of Object.entries(studentsBySubject)) {
      console.log(`Number of students in ${subject}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

