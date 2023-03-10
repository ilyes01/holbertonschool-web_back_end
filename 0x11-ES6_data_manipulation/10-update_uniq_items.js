function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw 'Cannot process';
  }
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  return map;
}

export default updateUniqueItems;
