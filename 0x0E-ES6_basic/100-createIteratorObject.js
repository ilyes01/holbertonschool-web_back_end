export default function createIteratorObject(report) {
    const departments = Object.keys(report);
    let currentDepartment = 0;
    let currentEmployee = 0;

    return {
        next: function () {
            const department = departments[currentDepartment];
            if (!department) {
                return { done: true };
            }
            const employees = report[department];
            if (currentEmployee >= employees.length) {
                currentEmployee = 0;
                currentDepartment++;
                return this.next();
            }
            return { value: employees[currentEmployee++], done: false };
        }
    };
}
