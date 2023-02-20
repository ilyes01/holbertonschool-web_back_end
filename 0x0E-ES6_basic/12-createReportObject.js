function createReportObject(employeesList) {
  const obj = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
  return obj;
}

export default createReportObject;
