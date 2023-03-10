export default function cleanSet(set, startString) {
  if (typeof startString === 'undefined') {
    return '';
  }

  let result = '';
  for (const item of set) {
    if (typeof item !== 'undefined' && item.startsWith(startString)) {
      if (result.length > 0) {
        result += '-';
      }
      result += item.slice(startString.length);
    }
  }
  return result;
}
