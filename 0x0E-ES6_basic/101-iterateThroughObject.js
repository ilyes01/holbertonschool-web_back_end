function iterateThroughObject(reportWithIterator) {
  const x = [...reportWithIterator];
  return x.join(' | ');
}

export default iterateThroughObject;
