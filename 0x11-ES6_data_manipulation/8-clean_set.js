export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') {
    return '';
  }

  const resultArr = [];
  for (const value of set) {
    if (typeof value !== 'string') {
      continue;
    }
    if (value.startsWith(startString)) {
      resultArr.push(value.slice(startString.length));
    }
  }

  return resultArr.join('-');
}
