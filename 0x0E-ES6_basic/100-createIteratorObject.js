export default function createIteratorObject(report) {
    return {
        [Symbol.iterator]: function* () {
            for (const department in report) {
                for (const employee of report[department]) {
                    yield employee;
                }
            }
        }
    }
}
