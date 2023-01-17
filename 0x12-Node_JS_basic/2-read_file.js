const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf-8');
        const lines = data.split('\n');
        let fields = {};
        for (let i = 0; i < lines.length; i++) {
            if (lines[i] !== '') {
                let student = lines[i].split(',');
                if (!fields[student[2]]) {
                    fields[student[2]] = { count: 1, list: [student[0]] };
                } else {
                    fields[student[2]].count++;
                    fields[student[2]].list.push(student[0]);
                }
            }
        }
        console.log(`Number of students: ${lines.length - 1}`);
        for (let field in fields) {
            console.log(`Number of students in ${field}: ${fields[field].count}. List: ${fields[field].list}`);
        }
    } catch (err) {
        console.log('Cannot load the database');
    }
}

module.exports = countStudents;
