export default function updateUniqueItems(itemMap) {
    if (typeof itemMap !== 'object') {
        throw new Error("Cannot process");
    }
    for (const key in itemMap) {
        if (itemMap[key] === 1) {
            itemMap[key] = 100;
        }
    }
    return itemMap;
}

